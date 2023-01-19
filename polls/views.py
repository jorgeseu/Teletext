from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from django.utils.decorators import method_decorator
from rest_framework import status, request

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Poll, Choice, Vote
from.serializers import PollSerializer, ChicesSerializer, VoteSerializer ,VoteCountSerializer
from annoucement.permissions import IsOwnerOrReadOnly
from django.db.models import Count
from django.db.models import Sum
#stats
from core.stats_helper import store_user_action


from django.http import JsonResponse

# Create your views here.

# polls list and create poll
class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#update and delete poll, only owner can modify
class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#choice list update and delete, only owner can modify
class ChoiceList(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, pk):
        queryset = Choice.objects.filter(poll = pk)
        serializer = ChicesSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        #stats
        current_user = request.user
        store_user_action(current_user.id, 'Poll posted')
        serializer = ChicesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        #serializer.save(poll=self.request.poll)

    # queryset = Choice.objects.all()
    # serializer_class = ChicesSerializer
    # #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #
    # def perform_create(self, serializer):
    #     serializer.save(poll=self.request.data['poll'])

#votes list and create vote on specific choice
class VoteList(APIView):

    def get(self, request, pk, id):
        queryset = Vote.objects.filter(poll = pk , choice = id)
        serializer = VoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, pk, id):
        #sprawdzic
        serializer = VoteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_voted = Vote.objects.filter(poll=pk,choice=id, vote_user = self.request.user.id)

        if not user_voted.exists():
            # stats
            current_user = request.user
            store_user_action(current_user.id, 'Post voted')
            #zmieniłem  serlaizer zeby zapisaywać usera z requesta (VoteSerializer)
            serializer.save(vote_user=self.request.user)

            return Response(serializer.data)

        else:
            return Response({"detail": "You can vote only once"}, status=status.HTTP_400_BAD_REQUEST)

#do wywalenia
# class VoteListCount(APIView):
#
#     def get(self, request, pk, id):
#         queryset = Vote.objects.filter(poll=pk, choice=id)
#         queryset.count()
#         return Response({"votes": queryset.count()})

#poll and choices info in one responce
class ComboPollView(APIView):

    def get(self, request ,pk):
        poll = Poll.objects.filter(id = pk)
        choices = Choice.objects.filter(poll = pk)
        votes = Vote.objects.filter(poll = pk)
        #votes_count = Vote.objects.filter(poll = pk, choice = 1)
        #choices.annotate(count=Count('choice'))

        poll_serializer = PollSerializer(poll, many=True)
        chices_serializer = ChicesSerializer(choices, many=True)
        #votes_serializer = VoteSerializer(votes, many=True)
        #votes_count_serializer = VoteCountSerializer(votes_count, many=True)

        return Response({
            'poll': poll_serializer.data,
            'choices': chices_serializer.data,

        })

#poll result and sum of votes in specific choice
class PollResult(APIView):
    def get(self, request, pk):

        choice = Choice.objects.filter(poll=pk)

        poll_results = []
        for item in choice:
            votes = Vote.objects.filter(poll=pk, choice=item.id).count()
            # print(item['choice_name'])
            poll_results.append({
                'choice':item.choice_name,
                'result':votes
            })

        print(poll_results)
        #..annotate(num_vote=Sum(''))

        chices_serializer = ChicesSerializer(choice, many=True)
       # result_serializer = VoteCountSerializer(votes, many=True)

        return Response({
            "result": poll_results
            #'choices': chices_serializer.data,
            #'result': votes_serializer.data,
        })