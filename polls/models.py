from django.db import models
from django.utils import timezone

import datetime
from accounts.models import UserData


class Poll(models.Model):
    user = models.ForeignKey(UserData, related_name='user', on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(Poll,related_name='poll', on_delete=models.CASCADE)
    choice_name = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_name

class Vote(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice,related_name='choice', on_delete=models.CASCADE)
    vote_user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    can_vote = models.BooleanField(default=True)

    # def user_can_vote(self, user):
    #     """
    #     Return False if user already voted
    #     """
    #     user_votes = user.vote_set.all()
    #     qs = user_votes.filter(poll=self)
    #     if qs.exists():
    #         return False
    #     return True

    # class Meta:
    #     unique_together = ("poll", "vote_user")

    # def __str__(self):
    #     return self.id