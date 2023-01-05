from django.urls import path, include
from django.contrib.auth import urls
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import RegisterView, UserDetail

from rest_framework_simplejwt.views import (
    #TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from .views import MyTokenObtainPairView




# in browser http://127.0.0.1:8000/accounts/api/token/ to login
urlpatterns = [
    # jwt login
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/register/', RegisterView.as_view(), name="sign_up"),
    #path('login/', include('django.contrib.auth.urls'))

    path('api/profile/<int:pk>/', UserDetail.as_view(), name='profile_detail' ),
    #path('api/api-auth/', include('rest_framework.urls')),


]