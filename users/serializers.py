from rest_framework import serializers

from .models import Payments, User


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True, read_only=True)  # Включаем платежи

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "is_active",
            "phone",
            "city",
            "avatar",
            "payments",
        ]
