from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from users.models import Payments, User


class UserSerializer(ModelSerializer):
    payments = SerializerMethodField()

    def get_payment_history(self, obj):
        return PaymentsSerializer(obj.payment_set.all(), many=True).data

    class Meta:
        model = User
        fields = "__all__"



class PaymentsSerializer(ModelSerializer):
    payment_history = SerializerMethodField()
    class Meta:
        model = Payments
        fields = "__all__"

