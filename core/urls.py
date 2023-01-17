from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from . import weatherview

urlpatterns = [
    path('', views.homepage),
    path('weather/', weatherview.weather_call),
    path('ProgramItems/', views.ProgramItems),
    path('ProgramItems/<int:pk>/', views.Program_detail),
    path('MODItems/', views.MODItems),
    path('MODItems/<int:pk>/', views.MOD_detail),
    path('StatItems/', views.StatItems),
    path('StatItems/<int:pk>/', views.Stat_detail),
    #path('gmailAuthenticate/', views.gmail_authenticate),
    #path('oauthcallback/', views.Program_detail),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
