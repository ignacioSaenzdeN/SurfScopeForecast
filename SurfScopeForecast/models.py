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
    secretList = models.TextField(blank=True)
    fantasyLeague = models.TextField(blank=True)
    alerts = models.TextField(blank=True)
