from rest_framework import viewsets
from .models import User, Payments
from .serializers import UserSerializer, PaymentsSerializer
from django_filters import rest_framework as filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentsFilter(filters.FilterSet):
    date_of_payment = filters.DateTimeFilter(field_name='date_of_payment', lookup_expr='exact')
    course = filters.NumberFilter(field_name='course__id')  # Фильтр по ID курса
    lesson = filters.NumberFilter(field_name='lesson__id')  # Фильтр по ID урока
    payment_method_is_cash = filters.BooleanFilter(field_name='payment_method_is_cash')

    class Meta:
        model = Payments
        fields = ['date_of_payment', 'course', 'lesson', 'payment_method_is_cash']

class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PaymentsFilter
    ordering_fields = ['date_of_payment']  # Поля, по которым можно сортировать
    ordering = ['date_of_payment']  # Поле по умолчанию для сортировки
