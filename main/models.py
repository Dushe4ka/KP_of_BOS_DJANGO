from django.db import models


class Message(models.Model):
    date_m = models.CharField(max_length=30, blank=True, null=True)
    info_m = models.CharField(max_length=30, blank=True, null=True)
    application_m = models.CharField(max_length=30, blank=True, null=True)
    action_m = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'
