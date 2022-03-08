from rest_framework import serializers
from LoginAPI.models import User
from .models import Location, Activity, Route
from ReviewAPI.serializers import FetchReviewSerializer
from PostAPI.serializers import GetPostSerializer

######################## USER ########################################
class GetUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'isAdmin')
        depth = 1
        
class GetAccountSerializer(serializers.ModelSerializer):
    user_post = GetPostSerializer(many=True, read_only=True,)
    user_review = FetchReviewSerializer(many=True, read_only=True,)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'isAdmin', 'user_post', 'user_review')
        depth = 1

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirmPassword', 'firstname', 'lastname', 'isAdmin')


    
######################## Activity ########################################
class GetActivitySerializer(serializers.ModelSerializer):
    activity_post = GetPostSerializer(many=True, read_only=True)
    activity_review = FetchReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Activity
        fields = ('id', 'discription', 'name', 'approach', 'height', 'difficulty', 'start_latitude', 'start_longitude','finish_latitude', 'finish_longitude', 'location', 'activity_post', 'activity_review')

class DeleteActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'name')

class CreateActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('discription', 'name', 'approach', 'height', 'difficulty', 'start_latitude', 'start_longitude','finish_latitude', 'finish_longitude')
        

######################## Location ########################################
class GetLocationSerializer(serializers.ModelSerializer):
    activity_post = GetPostSerializer(many=True, read_only=True)
    activity_review = FetchReviewSerializer(many=True, read_only=True)
    activity_location = GetActivitySerializer(many=True, read_only=True)
    class Meta:
        model = Location
        fields = ('id', 'discription', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode','altitude', 'activity_location','activity_post', 'activity_review')
        depth = 1

class DeleteLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class CreateLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('discription', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude')
