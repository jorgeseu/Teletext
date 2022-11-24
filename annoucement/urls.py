from django.urls import path, include
from .views import AnnoucementViev

urlpatterns = [
    #http://127.0.0.1:8000/ad/api/annoucements
    path('api/annoucements', AnnoucementViev.as_view(), name='annoucement_list_all'),

]