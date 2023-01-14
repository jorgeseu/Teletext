from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Poll, Choice, Vote

class PollSerializer(ModelSerializer):
    #z with owner there works
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Poll
        fields = ['id','user','question', 'pub_date']


class ChicesSerializer(ModelSerializer):
    #poll = serializers.ReadOnlyField(source='poll.question')

    class Meta:
        model = Choice
        fields = ['id', 'poll', 'choice_name']


class VoteSerializer(ModelSerializer):
    #choice = serializers.ReadOnlyField(source='choice.choice_name')
    #poll = serializers.ReadOnlyField(source='poll.question')
    #vote_user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Vote
        fields = ['id', 'poll', 'choice', 'can_vote']

class VoteCountSerializer(ModelSerializer):
   # choice = serializers.ReadOnlyField(source='choice.choice_name')
    #poll = serializers.ReadOnlyField(source='poll.question')
    #vote_count = serializers.IntegerField(source='vote.count', read_only=True)


    class Meta:
        model = Vote
        fields = ['choice', 'result ']