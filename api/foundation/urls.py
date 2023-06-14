from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.foundation.views import (
    LoginAPIView,
    LogoutView,
    RegisterationAPIView
)

app_name = "api.foundation"

router = DefaultRouter()


urlpatterns = [
    # Login apis
    path("auth/register/", RegisterationAPIView.as_view(), name="user_register"),
    path("auth/login/", LoginAPIView.as_view(), name="user_login"),
    path("auth/logout/", LogoutView.as_view(), name="auth_logout"),
    # Token apis
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
]

urlpatterns += router.urls
