import json
from datetime import datetime, timedelta

import stripe
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(prod):
    """Создает продукт в страйпе"""
    product = prod.course if prod.course else prod.lesson
    stripe_product = stripe.Product.create(name=product)
    return stripe_product.get("id")


def create_stripe_price(amount, product_id):
    """Создает цену в страйпе"""
    return stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product_data={"name": product_id},
    )


def create_stripe_sessions(price):
    """Создает сессию на оплату в страйпе"""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
