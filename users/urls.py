from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PaymentsViewSet, UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"payments", PaymentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
