# backend/modules/booking/pricing_service.py

import requests

def get_current_fee():
    url = "https://rikkijprince.com/fee.json"
    response = requests.get(url, timeout=5)
    data = response.json()
    return data["price_eur"]
    
def get_current_session_length():
    url = "https://rikkijprince.com/fee.json"
    response = requests.get(url, timeout=5)
    data = response.json()
    return data["session_length"]
