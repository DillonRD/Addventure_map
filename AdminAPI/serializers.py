from rest_framework import serializers
from LoginAPI.models import User
from ReviewAPI.models import Review
from .models import Location, Activity, Route, Post


######################## Post ########################################
class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'activity', 'location', 'user', 'photo', 'created', 'updated', 'likes', 'tex')

class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'password')
        
######################## Review ########################################
class GetReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'activity', 'location', 'user', 'photo', 'created', 'updated', 'rating', 'tex')

######################## USER ########################################
class GetUserSerializer(serializers.ModelSerializer):
    posts = GetPostSerializer(read_only=True, many=True)
    review = GetReviewSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'isAdmin')
        depth = 1
        
class GetAccountSerializer(serializers.ModelSerializer):
    posts = GetPostSerializer(read_only=True, many=True)
    review = GetReviewSerializer(read_only=True, many=True)
    class Meta:
        model = User
        depth = 1
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'isAdmin', 'posts', 'review')
        depth = 1

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirmPassword', 'firstname', 'lastname', 'isAdmin')


    
######################## Activity ########################################
class GetActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'discription', 'name', 'approach', 'height', 'difficulty', 'start_latitude', 'start_longitude','finish_latitude', 'finish_longitude', 'location')

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
    activity = GetActivitySerializer(read_only=True, many=True)
    class Meta:
        model = Location
        fields = ('id', 'discription', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode','altitude')
        depth = 1

class DeleteLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'name')

class CreateLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('discription', 'name', 'latitude', 'longitude', 'address', 'city', 'zipcode', 'altitude')
