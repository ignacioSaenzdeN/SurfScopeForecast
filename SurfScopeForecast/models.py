from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Blackbox(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)
    newfield = models.CharField(max_length=500, default='some string')


class SurfingInfo(models.Model):
    ID = models.TextField(unique=True)
    #secretList = models.TextField(blank=True)
    secretList = models.JSONField(default="{}")
    fantasyLeague = models.TextField(blank=True)
    alerts = models.TextField(blank=True)

# class Example(models.Model):
#     # Default has to be immutable otherwise it will be passed by reference
#     # and all data created in the same session all will have the same reference
#     # must pass string
#     data = models.JSONField()
