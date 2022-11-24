from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserData

# Create your models here.


class Annoucement_category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class Annoucement(models.Model):
    user =models.ForeignKey(UserData, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    category_name = models.ForeignKey(Annoucement_category, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


