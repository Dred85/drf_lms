from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from .models import Payments, User
from .serializers import PaymentsSerializer, UserSerializer
from .services import create_stripe_product, create_stripe_price, create_stripe_sessions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)

    # Фильтрация по полям
    filterset_fields = ("course", "lesson", "payment_method_is_cash")

    # Фильтрация по дате
    ordering_fields = ("date_of_payment",)

    # Поле по умолчанию для сортировки
    ordering = ("date_of_payment",)

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product_id = create_stripe_product(payment)
        price = create_stripe_price(payment.amount, product_id)
        session_id, payment_link = create_stripe_sessions(price)
        payment.session_id = session_id
        payment.link_to_payment = payment_link
        payment.save()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (
        AllowAny,
    )  # Даем доступ для всех не авторизованных пользователей

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
