from django.contrib.auth import get_user_model
from jsonfield import JSONField
from django.db import models
# Create your models here.


class Blackbox(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)
    newfield = models.CharField(max_length=500, default='some string')


class SurfingInfo(models.Model):
    ID = models.TextField(unique=True)
    username = models.TextField(default="")
    secretList = JSONField(default="{}")
    fantasyLeague = models.TextField(blank=True)
    alerts = models.TextField(blank=True)
    boardSuggestion = models.TextField(blank=True)
    wetSuitSuggestion = models.TextField(blank=True)
    totalTeamScore = models.TextField(default="0")


class Boardshorts(models.Model):
    itemType = models.TextField(default="")
    imageUrl = models.TextField(default="")
    productUrl = models.TextField(default="")


class Wetsuits(models.Model):
    itemType = models.TextField(default="")
    imageUrl = models.TextField(default="")
    productUrl = models.TextField(default="")
    legs = models.TextField(default="")
    thickness = models.TextField(default="")
    zipperType = models.TextField(default="")


class Surfboards(models.Model):
    itemType = models.TextField(default="")
    imageUrl = models.TextField(default="")
    productUrl = models.TextField(default="")
    dimensions = models.TextField(default="")
    volume = models.TextField(default="")


class UserWetsuit(models.Model):
    user = models.ForeignKey(
        SurfingInfo, on_delete=models.CASCADE, related_name='wetsuit')
    gender = models.TextField(default="")
    size = models.TextField(default="")
    waterTemp = models.TextField(default="")
    coldSensitivy = models.TextField(default="")
    zipperType = models.TextField(default="")
    imageUrl = models.TextField(default="")
    productUrl = models.TextField(default="")


class UserSurfboard(models.Model):
    user = models.ForeignKey(
        SurfingInfo, on_delete=models.CASCADE, related_name='surfboard')
    weight = models.TextField(default="")
    height = models.TextField(default="")
    size = models.TextField(default="")
    level = models.TextField(default="")
    waveSize = models.TextField(default="")
    imageUrl = models.TextField(default="")
    productUrl = models.TextField(default="")

# class Example(models.Model):
#     # Default has to be immutable otherwise it will be passed by reference
#     # and all data created in the same session all will have the same reference
#     # must pass string
#     data = models.JSONField()
