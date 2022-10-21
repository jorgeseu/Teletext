from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import weatherview

urlpatterns = [
    path('', views.homepage),
    path('weather/', weatherview.weather_call),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
