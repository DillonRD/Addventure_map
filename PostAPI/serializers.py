from rest_framework import serializers
from .models import Post


######################## Post ########################################
class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'activity', 'location', 'user', 'photo', 'created', 'updated', 'likes', 'text')

        
class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('photo', 'likes', 'text')
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('activity', 'location', 'user', 'photo', 'created', 'updated', 'likes', 'text')