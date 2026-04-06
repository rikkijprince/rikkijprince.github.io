```python
from flask import Flask, request, jsonify
import json
import os
from datetime import datetime
import stripe

app = Flask(__name__)

# CONFIG
STRIPE_SECRET_KEY = "sk_live_..."
STRIPE_WEBHOOK_SECRET = "whsec_..."

stripe.api_key = STRIPE_SECRET_KEY

USERS_FILE = "users.json"


# -------------------------
# Helpers
# -------------------------

def load_users():
    if not os.path.exists(USERS_FILE):
        return {"users": []}
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f, indent=4)


def find_user_by_email(email):
    data = load_users()
    for user in data["users"]:
        if user["email"] == email:
            return user
    return None


def update_user(email, updates):
    data = load_users()

    for user in data["users"]:
        if user["email"] == email:
            user.update(updates)

    save_users(data)


# -------------------------
# API: Get user (secure)
# -------------------------

@app.route("/api/get_user", methods=["POST"])
def api_get_user():
    data = request.json
    email = data.get("email")

    user = find_user_by_email(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


# -------------------------
# API: Add user
# -------------------------

@app.route("/api/add_user", methods=["POST"])
def api_add_user():
    data = request.json

    users = load_users()

    # prevent duplicates
    for u in users["users"]:
        if u["email"] == data["email"]:
            return jsonify({"message": "User exists"}), 200

    new_user = {
        "username": data["username"],
        "email": data["email"],
        "phone": data.get("phone"),
        "signup_date": datetime.now().strftime("%Y-%m-%d"),
        "status": "basic_free",
        "upgrade_basic_price": None,
        "upgrade_full_price": None
    }

    users["users"].append(new_user)
    save_users(users)

    return jsonify({"message": "User created"}), 201


# -------------------------
# STRIPE WEBHOOK
# -------------------------

@app.route("/webhook", methods=["POST"])
def stripe_webhook():

    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except Exception as e:
        return str(e), 400

    # PAYMENT SUCCESS
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        email = session.get("customer_details", {}).get("email")
        amount = session.get("amount_total", 0) / 100

        if email:
            if amount == 1000:
                update_user(email, {
                    "status": "basic_paid",
                    "upgrade_basic_price": amount
                })
            elif amount == 2000:
                update_user(email, {
                    "status": "full_paid",
                    "upgrade_full_price": amount
                })

    return jsonify({"status": "success"})

# Admin dashboard
@app.route("/api/all_users", methods=["GET"])
def get_all_users():
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 403

    data = load_users()
    return jsonify(data)
```
