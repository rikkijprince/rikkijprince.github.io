from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import stripe

from modules.booking.calendar_service import (
    get_available_slots,
    format_slots,
    create_tentative_event,
    confirm_event,
    cancel_event,
    is_slot_still_available
)
from modules.booking.pricing_service import get_current_fee
from modules.booking.payment_service import create_checkout_session
from modules.users.user_store import get_or_create_user, add_booking_to_user

app = FastAPI()

# Allow your website to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development; restrict to your domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# 1️⃣ Get Available Slots
# -------------------------
@app.get("/slots")
def get_slots():
    raw_slots = get_available_slots()
    formatted_slots = format_slots(raw_slots)
    return [
        {
            "display": slot["display"],
            "datetime": slot["datetime"].isoformat()
        }
        for slot in formatted_slots
    ]


# -------------------------
# 2️⃣ Create Booking
# -------------------------
class BookingRequest(BaseModel):
    full_name: str
    email: str
    phone: str | None = None
    slot: str


@app.post("/create-web-booking")
def create_web_booking(request: BookingRequest):
    selected_slot = datetime.fromisoformat(request.slot)

    if not is_slot_still_available(selected_slot):
        raise HTTPException(status_code=400, detail="Slot no longer available")

    # Create or retrieve user
    user = get_or_create_user(
        full_name=request.full_name,
        email=request.email,
        phone=request.phone
    )

    # Create tentative calendar event
    event_id = create_tentative_event(user, selected_slot)

    # Create Stripe checkout session
    fee = get_current_fee()
    checkout_url, session_id = create_checkout_session(
        amount=fee,
        metadata={
            "event_id": event_id,
            "email": request.email
        }
    )

    # Save booking to user record
    add_booking_to_user(request.email, {
        "event_id": event_id,
        "slot": selected_slot.isoformat(),
        "payment_status": "pending",
        "session_id": session_id,
        "amount": fee,
        "currency": "EUR",
        "created_at": datetime.utcnow().isoformat()
    })

    return {"checkout_url": checkout_url}


# -------------------------
# 3️⃣ Stripe Webhook
# -------------------------
stripe.api_key = "YOUR_STRIPE_SECRET_KEY"
endpoint_secret = "YOUR_STRIPE_WEBHOOK_SECRET"


@app.post("/stripe-webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    session = event["data"]["object"]
    metadata = session.get("metadata", {})
    event_id = metadata.get("event_id")

    if event["type"] == "checkout.session.completed":
        confirm_event(event_id)
    elif event["type"] in ["checkout.session.expired", "payment_intent.payment_failed"]:
        cancel_event(event_id)

    return {"status": "success"}
