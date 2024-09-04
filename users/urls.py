from django.urls import path

from users.apps import UsersConfig
from users.views import (
    UserRetrieveUpdateAPIView,
    UserListAPIView,
    PaymentsListAPIView,
    PaymentsRetrieveAPIView,
    PaymentsCreateAPIView,
    PaymentsUpdateAPIView,
    PaymentsDestroyAPIView,
)

app_name = UsersConfig.name


urlpatterns = [
    path(
        "users/<int:pk>/retrieve_update/",
        UserRetrieveUpdateAPIView.as_view(),
        name="users_retrieve_update",
    ),
    path("users/create/", UserCreateAPIView.as_view(), name="users_create"),
    path("users/<int:pk>/delete/", UserDestroyAPIView.as_view(), name="users_delete"),
    path("users/", UserListAPIView.as_view(), name="users"),

    # payments
    path("payments/", PaymentsListAPIView.as_view(), name="payments"),
    path(
        "payments/<int:pk>/",
        PaymentsRetrieveAPIView.as_view(),
        name="payments_retrieve",
    ),
    path("payments/create/", PaymentsCreateAPIView.as_view(), name="payments_create"),
    path(
        "payments/<int:pk>/update/",
        PaymentsUpdateAPIView.as_view(),
        name="payments_update",
    ),
    path(
        "payments/<int:pk>/delete/",
        PaymentsDestroyAPIView.as_view(),
        name="payments_delete",
    ),
]