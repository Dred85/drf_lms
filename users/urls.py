from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import PaymentsViewSet, UserViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"payments", PaymentsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
