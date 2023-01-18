from django.db import models

class Action(models.Model):
    user = models.CharField()
    date = models.DateField()
    action = models.CharField(max_length=255)