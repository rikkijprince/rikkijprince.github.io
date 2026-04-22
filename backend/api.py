#backend\api.py

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

from backend.modules.booking.calendar_service import (
    get_available_slots,
    format_slots,
    is_slot_still_available,
    create_tentative_event
)

from backend.modules.booking.pricing_service import get_current_fee
from backend.modules.booking.payment_service import create_checkout_session

app = FastAPI()


class BookingRequest(BaseModel):
    slot: str
    user: dict


@app.get("/api/slots")
def api_slots():
    raw = get_available_slots()
    return format_slots(raw)


@app.get("/api/price")
def api_price():
    return {"fee": get_current_fee()}


@app.post("/api/book")
def api_book(req: BookingRequest):
    selected_slot = datetime.fromisoformat(req.slot)

    if not is_slot_still_available(selected_slot):
        return {"error": "Slot just taken. Please choose another."}

    event_id = create_tentative_event(req.user, selected_slot)
    fee = get_current_fee()

    checkout_url, session_id = create_checkout_session(
        amount=fee,
        metadata={
            "event_id": event_id,
            "user": req.user.get("name", "Guest")
        }
    )

    return {"checkout_url": checkout_url}
