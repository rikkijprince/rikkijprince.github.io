# backend/modules//booking/pricing_service.py

import json
import os

FEE_FILE = os.path.join(os.path.dirname(__file__), "fee.json")


def read_fee_file():
    try:
        with open(FEE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print("❌ Cannot read fee.json:", e)
        return {
            "price_eur": 0,
            "session_length": 0
        }


def get_pricing():
    data = read_fee_file()
    return {
        "price_eur": data.get("price_eur"),
        "session_length": data.get("session_length")
    }


def get_session_price():
    return read_fee_file().get("price_eur")


def get_session_length():
    return read_fee_file().get("session_length")
