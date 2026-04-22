# api.py
from fastapi import FastAPI
from book_classes import (
    get_available_slots,
    format_slots,
    create_tentative_event,
    create_checkout_session,
    is_slot_still_available,
    get_current_fee
)

app = FastAPI()

@app.get("/api/slots")
def get_slots():
    raw = get_available_slots()
    return format_slots(raw)


@app.post("/api/book")
def book_slot(data: dict):
    selected_slot = data["slot"]
    user = data["user"]

    if not is_slot_still_available(selected_slot):
        return {"error": "Slot taken"}

    event_id = create_tentative_event(user, selected_slot)
    fee = get_current_fee()

    checkout_url, session_id = create_checkout_session(
        amount=fee,
        metadata={
            "event_id": event_id,
            "user": user["name"]
        }
    )

    return {
        "checkout_url": checkout_url
    }
