from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PaymentsViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"payments", PaymentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
