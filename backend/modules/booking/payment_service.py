# backend/modules/booking/payment_service.py

import os
import stripe
from dotenv import load_dotenv

load_dotenv()

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

if not stripe.api_key:
    raise ValueError("Missing STRIPE_SECRET_KEY")


def create_checkout_session(amount, metadata):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "eur",
                "product_data": {
                    "name": "Fluency Coaching Session",
                },
                "unit_amount": int(amount * 100),
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url="https://yourdomain.com/success",
        cancel_url="https://yourdomain.com/cancel",
        metadata=metadata,
    )

    return session.url, session.id
