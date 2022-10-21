from django.db import models
from django.contrib.auth.models import User
from django.db import models
from oauth2client.contrib.django_util.models import CredentialsField

# Create your models here.

class CredentialsModel(models.Model):
    id = models.ForeignKey(User, primary_key = True, on_delete = models.CASCADE)
    credential = CredentialsField()
    task - models.CharField(max_length = 80, null = True)
    updated_time = models.CharField(max_length = 80, null = True)

class CredentialsAdmin(admin.ModelAdmin): # agora quem vai saber
    pass