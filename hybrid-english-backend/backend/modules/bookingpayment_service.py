import stripe
import os

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout_session(amount, metadata):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "eur",
                "product_data": {
                    "name": "Fluency Coaching Session"
                },
                "unit_amount": int(amount * 100),  # Convert euros to cents
            },
            "quantity": 1,
        }],
        metadata=metadata,
        success_url="https://rikkijprince.com/success",
        cancel_url="https://rikkijprince.com/cancel",
    )

    return session.url, session.id
