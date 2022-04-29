from rest_framework import serializers
from ActivityAPI.serializers import FetchActivitySerializer
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('description', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude')


class FetchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'description', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude')

class FetchLocationsSerializer(serializers.ModelSerializer):
    location_post = FetchActivitySerializer(many=True, read_only=True,)
    
    class Meta:
        model = Location
        fields = ('id', 'description', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude', 'location_post')
        depth = 1
       