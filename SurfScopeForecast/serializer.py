from rest_framework import serializers
from . models import *


class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blackbox
        fields = ['name', 'detail', 'newfield']

class SurfingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurfingInfo
        fields = ['id','ID', 'secretList', 'fantasyLeague', 'alerts']


