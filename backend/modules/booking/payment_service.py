# backend/modules/booking/payment_service.py

import stripe
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

def create_checkout_session(amount, metadata):
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': 'Fluency Coaching Session'
                },
                'unit_amount': int(amount * 100),
            },
            'quantity': 1,
        }],
        mode='payment',

        success_url='https://rikkijprince.com/success',
        cancel_url='https://rikkijprince.com/cancel',

        metadata=metadata
    )

    return session.url, session.id



def check_payment_status(session_id):
    session = stripe.checkout.Session.retrieve(session_id)
    return "paid" if session.payment_status == "paid" else "pending"
