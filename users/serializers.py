from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from users.models import Payments, User


class UserSerializer(ModelSerializer):
    payments = SerializerMethodField()

    def get_payments(self, obj):
        return [
            f"{p.date_of_payment}-({p.payment_amount}, наличные: {p.payment_method_is_cash}),"
            for p in Payments.objects.filter(user=obj).order_by("date_of_payment")
        ]

    class Meta:
        model = User
        fields = "__all__"

class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"

    def create(self, validated_data):
        if validated_data.get("course") and validated_data.get("lesson"):
            raise ValidationError(
                "You can choose 'course' or 'lesson', but not both at the same time"
            )
        elif (
            validated_data.get("course") is None
            and validated_data.get("lesson") is None
        ):
            raise ValidationError("You must choose 'course' or 'lesson'")

        payment_item = Payments.objects.create(**validated_data)
        return payment_item

    def update(self, instance, validated_data):
        if validated_data.get("course") and validated_data.get("lesson"):
            raise ValidationError(
                "You can choose 'course' or 'lesson', but not both at the same time"
            )
        elif (
            validated_data.get("course") is None
            and validated_data.get("lesson") is None
        ):
            raise ValidationError("You must choose 'course' or 'lesson'")

        payment_item = Payments.objects.create(**validated_data)
        return payment_item