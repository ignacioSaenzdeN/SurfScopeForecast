from rest_framework import serializers
from ..models import *


class FantasyLeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyLeague
        fields = ['rank', 'name', 'country_name', 'tour_points',
                  'athlete_country_flag', 'athlete_photo', 'gender']
