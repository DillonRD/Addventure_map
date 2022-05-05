from rest_framework import serializers
from LoginAPI.models import User
from ReviewAPI.serializers import FetchReviewSerializer
from PostAPI.serializers import GetPostSerializer


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'address', 'city',
                  'zipcode', 'latitude', 'longitude')

        
        
class GetAccountSerializer(serializers.ModelSerializer):
    user_post = GetPostSerializer(many=True, read_only=True,)
    user_review = FetchReviewSerializer(many=True, read_only=True,)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'isAdmin', 'user_post', 'user_review')
        depth = 1
        
class DeleteUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')