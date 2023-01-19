from django.db import models

class Action(models.Model):
    user = models.CharField(max_length=200)
    date = models.DateField(max_length=200)
    action = models.CharField(max_length=255)

    def __str__(self):
        return self.action