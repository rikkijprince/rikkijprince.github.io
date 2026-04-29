# backend/modules//booking/pricing_service.py

import json
import os

FEE_FILE = os.path.join(os.path.dirname(__file__), "fee.json")


def get_pricing():
    with open(FEE_FILE, "r") as f:
        return json.load(f)


def get_current_fee():
    return get_pricing()["price_eur"]
