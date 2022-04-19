from rest_framework import serializers
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('description', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude')


class FetchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'description', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude')
