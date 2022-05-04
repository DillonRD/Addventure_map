from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('description', 'name', 'approach', 'altitude', 'height', 'difficulty', 'start_latitude'
                  , 'start_longitude', 'finish_latitude', 'finish_longitude', 'location')


class FetchActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('description', 'name', 'approach', 'altitude', 'height', 'difficulty', 'start_latitude',
         'start_longitude', 'finish_latitude', 'finish_longitude')
