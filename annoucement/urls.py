from django.urls import path, include
from .views import AnnoucementViev, AnnoucementUpdateView, AnnoucementDetail

urlpatterns = [
    #http://127.0.0.1:8000/ad/api/annoucements
    path('api/annoucements', AnnoucementViev.as_view(), name='annoucement_list_all'),
    #http://127.0.0.1:8000/ad/api/annoucements/1/update
    path('api/annoucements/<pk>/update', AnnoucementDetail.as_view(), name='annoucement_update'),
    #path('api/annoucements/<pk>/delete', AnnoucementDeleteView.as_view(), name='annoucement_delete'),

]