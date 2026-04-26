# backend/modules/booking/booking_store.py

import json
import os
from datetime import datetime

STORE_FILE = "booking_store.json"


def _load_store():
    if not os.path.exists(STORE_FILE):
        return {}
    with open(STORE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_store(data):
    with open(STORE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# =========================
# PUBLIC API
# =========================

def save_booking(session_id, booking_data):
    store = _load_store()

    store[session_id] = {
        **booking_data,
        "created_at": datetime.utcnow().isoformat(),
        "status": "pending"
    }

    _save_store(store)


def get_booking(session_id):
    store = _load_store()
    return store.get(session_id)


def update_booking_status(session_id, status):
    store = _load_store()

    if session_id in store:
        store[session_id]["status"] = status
        store[session_id]["updated_at"] = datetime.utcnow().isoformat()
        _save_store(store)


def delete_booking(session_id):
    store = _load_store()

    if session_id in store:
        del store[session_id]
        _save_store(store)


def cleanup_expired_bookings(timeout_minutes=30):
    """
    Optional: remove stale unpaid bookings
    """
    store = _load_store()
    now = datetime.utcnow()

    updated = {}

    for sid, data in store.items():
        created = datetime.fromisoformat(data["created_at"])
        delta = (now - created).total_seconds() / 60

        if delta < timeout_minutes:
            updated[sid] = data

    _save_store(updated)
