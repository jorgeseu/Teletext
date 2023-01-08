from django.db import models

class Stat_item(models.Model):
    stat_ID = models.AutoField(primary_key=True)
    stat_message = models.CharField(max_length=200)
    stat_user = models.CharField(max_length=200)
    stat_datetime = models.DateTimeField(default=datetime.now())


    class Meta:
        verbose_name_plural = "stat_message"
    def __str__(self):
        return self.stat_ID