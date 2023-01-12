from django.urls import path, include
from .views import PollList, PollDetail, ChoiceList ,VoteList , ComboPollView ,VoteListCount ,PollResult

urlpatterns = [
    #http://127.0.0.1:8000/polls/api/polls
    path('api/polls/', PollList.as_view(), name='polls_list_all'),
    path('api/polls/<int:pk>', PollDetail.as_view(), name='poll_detail'),
    path('api/polls/<int:pk>/choices/', ChoiceList.as_view(), name='poll_detail'),
    path('api/polls/<int:pk>/choices/<int:id>', VoteList.as_view(), name='poll_detail'),
    path('api/polls/<int:pk>/choices/<int:id>/vote', VoteListCount.as_view(), name='poll_detail'),
    path('api/polls/combo/<int:pk>', ComboPollView.as_view(), name='poll_detail'),
    path('api/polls/combo/<int:pk>/result', PollResult.as_view(), name='poll_detail'),



]