from rest_framework import serializers
from . models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blackbox
        fields = ['name', 'detail', 'newfield']


class SurfingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfingInfo
        fields = ['id', 'ID', 'username',
                  'secretList', 'fantasyLeague', 'alerts', 'boardSuggestion', 'wetSuitSuggestion', 'totalTeamScore']


class SurfboardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surfboards
        fields = ['id', 'itemType', 'dimensions',
                  'volume', 'imageUrl', 'productUrl']


class WetsuitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wetsuits
        fields = ['id', 'itemType', 'sleeves',
                  'legs', 'thickness', 'zipperType']


class BoardShortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boardshorts
        fields = ['id', 'itemType', 'imageUrl',
                  'productUrl']


class UserWetsuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWetsuit
        fields = ['user', 'gender', 'size',
                  'waterTemp', 'coldSensitivy', 'zipperType', 'imageUrl', 'productUrl']


class UserSurfboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSurfboard
        fields = ['user', 'weight', 'height',
                  'size', 'level', 'waveSize', 'imageUrl', 'productUrl']
