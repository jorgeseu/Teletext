from django.db import models
from django.contrib.auth.models import User
from mod_models import MOD_item
from stat import Stat_item
#from oauth2client.contrib.django_util.models import CredentialsField
#from django.core.urlresolvers import reverse
class ProgramItem(models.Model):
	program_ID = models.CharField(max_length=200)
	program_date = models.DateField()
	program_data = models.TextField()

	class Meta:
		verbose_name_plural = "Program data"
		unique_together = ('program_ID', 'program_date',)

	def __str__(self):
		return self.program_ID


#class gCredentialsModel(models.Model):
#    id = models.ForeignKey(User, primary_key = True, on_delete = models.CASCADE)
#    credential = CredentialsField()
#    task - models.CharField(max_length = 80, null = True)
#    updated_time = models.CharField(max_length = 80, null = True)

#class CredentialsAdmin(admin.ModelAdmin):
#    pass