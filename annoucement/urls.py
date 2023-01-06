from django.urls import path, include
from .views import AnnoucementViev, AnnoucementUpdateAndDelete , AnnoucementCategory, AnnoucementsByCategory ,AnnoucementList
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/ad/api/annoucements
    path('api/annoucements', AnnoucementList.as_view(), name='annoucement_list_all'),

    #http://127.0.0.1:8000/ad/api/annoucements/1
    path('api/annoucements/<int:pk>', AnnoucementUpdateAndDelete.as_view(), name='annoucement_update'),
    path('api/annoucements/category/', AnnoucementCategory.as_view(), name='annoucement_by_category'),
    path('api/annoucements/category/<int:id>', AnnoucementsByCategory.as_view(), name='anno'),


    #test  git
   # path('api/annoucements/test', AnnoucementList.as_view(), name='annoucement_list'),

    #path('api/annoucements/<pk>/delete', AnnoucementDeleteView.as_view(), name='annoucement_delete'),

]