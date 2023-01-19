from django.db import models

class MOD_item(models.Model):
    message_ID  = models.IntegerField(primary_key=True, default=1)
    message_date = models.DateField("day for a message")
    message_content = models.TextField()

    class Meta:
        verbose_name_plural = "message_content"

    def __str__(self):
        return self.message_content