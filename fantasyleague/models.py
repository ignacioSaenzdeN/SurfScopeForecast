from django.db import models

# FantasyLeague model creates the structure of how a FantasyLeague
# team would look like


class FantasyLeague(models.Model):
    rank = models.TextField(default="")
    name = models.TextField(default="")
    country_name = models.TextField(default="")
    tour_points = models.TextField(default="")
    athlete_country_flag = models.TextField(default="")
    athlete_photo = models.TextField(default="")
    gender = models.TextField(default="")
