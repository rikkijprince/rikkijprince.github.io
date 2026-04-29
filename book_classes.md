# backend/api.py

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from datetime import datetime
import requests

from backend.modules.booking.calendar_service import (
    get_available_slots,
    format_slots,
    is_slot_still_available,
    create_tentative_event
)

from backend.modules.booking.pricing_service import get_pricing
from backend.modules.booking.payment_service import create_checkout_session

app = FastAPI()


# ============================
# CONFIG
# ============================

SUPABASE_URL = "https://ernxbalkjqrlngnumsuh.supabase.co"


# ============================
# MODELS
# ============================

class BookingRequest(BaseModel):
    slot: str


# ============================
# AUTH VALIDATION
# ============================

def verify_user(authorization: str):
    """
    Verifies Supabase JWT by calling Supabase Auth API.
    """

    if not authorization:
        raise HTTPException(status_code=401, detail="Missing auth token")

    try:
        token = authorization.split(" ")[1]  # Bearer <token>
    except:
        raise HTTPException(status_code=401, detail="Invalid auth header")

    res = requests.get(
        f"{SUPABASE_URL}/auth/v1/user",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    if res.status_code != 200:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return res.json()


# ============================
# ROUTES
# ============================

@app.get("/api/slots")
def api_slots():
    raw = get_available_slots()
    return format_slots(raw)


@app.get("/api/price")
def api_price():
    return get_pricing()


@app.post("/api/book")
def api_book(req: BookingRequest, authorization: str = Header(None)):

    # 🔐 Verify user
    user = verify_user(authorization)

    selected_slot = datetime.fromisoformat(req.slot)

    if not is_slot_still_available(selected_slot):
        return {"error": "Slot just taken. Please choose another."}

    # Use REAL authenticated user
    user_name = user.get("email", "User")

    event_id = create_tentative_event(
        {"name": user_name},
        selected_slot
    )

    pricing = get_pricing()

    checkout_url, session_id = create_checkout_session(
        amount=pricing["price_eur"],
        metadata={
            "event_id": event_id,
            "user": user_name
        }
    )

    return {
        "checkout_url": checkout_url,
        "event_id": event_id
    }
