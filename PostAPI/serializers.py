from rest_framework import serializers
from .models import Post


######################## Post ########################################
class GetPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'activity', 'location', 'user', 'photo', 'created', 'updated', 'likes', 'text')

class DeletePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'password')