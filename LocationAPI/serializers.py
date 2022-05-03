from rest_framework import serializers
from ActivityAPI.serializers import ActivitySerializer
from ReviewAPI.serializers import ReviewSerializer
from PostAPI.serializers import UserPostSerializer
from .models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('description', 'name', 'lat', 'lng', 'address', 'city', 'zipcode', 'altitude')


class FetchLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'description', 'name', 'lat', 'lng', 'address', 'city', 'zipcode', 'altitude')

class FetchCordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id','lat', 'lng')
       
class FetchAllSerializer(serializers.ModelSerializer):
    
    location_review = ReviewSerializer(required=True, many=True)
    location_post = UserPostSerializer(many=True, read_only=True)
    
    class Meta:
        model = Location
        fields = ('id', 'description', 'name', 'lat', 'lng', 'address', 'city', 'zipcode', 'location_post', 'location_review')
        depth = 1