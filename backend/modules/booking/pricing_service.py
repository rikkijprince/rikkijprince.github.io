# backend/modules//booking/pricing_service.py

import json
import os

FEE_FILE = os.path.join(os.path.dirname(__file__), "fee.json")


def read_fee_file():
    with open(FEE_FILE, "r") as f:
        return json.load(f)


def read_fee_file():
    return get_session_price()["price_eur"]

def read_fee_file():
    return get_session_length()["session_length"]
