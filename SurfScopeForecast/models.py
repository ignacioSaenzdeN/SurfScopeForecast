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


# class Example(models.Model):
#     # Default has to be immutable otherwise it will be passed by reference
#     # and all data created in the same session all will have the same reference
#     # must pass string
#     data = models.JSONField()
