from django.db import models
from django.contrib.auth.models import User
from django.db import models
#from oauth2client.contrib.django_util.models import CredentialsField

class ProgramItem(models.Model):
	program_ID = models.CharField(max_length=200)
	program_date = models.DateField()
	program_data = models.CharField()

	class Meta:
		verbose_name_plural = "Program data"
		unique_together = ('program_ID', 'program_date',)

	def __str__(self):
		return self.program_ID

# Create your models here.

#class CredentialsModel(models.Model):
#    id = models.ForeignKey(User, primary_key = True, on_delete = models.CASCADE)
#    credential = CredentialsField()
#    task - models.CharField(max_length = 80, null = True)
#    updated_time = models.CharField(max_length = 80, null = True)

#class CredentialsAdmin(admin.ModelAdmin): # agora quem vai saber
#    pass