# services/payment_service.py
import stripe
from app.models.order import Order
from app.models.user import User
from app.models.product import Product

stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"  # Replace with your actual Stripe secret key

def process_payment(order: Order, payment_method_id: str):
    """Process payment for an order using Stripe."""
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=order.total_amount(),  # Amount in the smallest unit (e.g., cents)
            currency='usd',
            payment_method=payment_method_id,
            confirm=True
        )
        order.status = "Paid"
        order.save()
        return payment_intent
    except stripe.error.CardError as e:
        order.status = "Failed"
        order.save()
        raise ValueError(f"Card error: {e.user_message}")
    except Exception as e:
        order.status = "Failed"
        order.save()
        raise ValueError(f"Payment processing error: {str(e)}")

def refund_payment(payment_intent_id: str):
    """Refund a payment using Stripe."""
    try:
        refund = stripe.Refund.create(payment_intent=payment_intent_id)
        return refund
    except Exception as e:
        raise ValueError(f"Refund error: {str(e)}")
