from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)


# in browser http://127.0.0.1:8000/accounts/token/
urlpatterns = [
    # jwt login
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]