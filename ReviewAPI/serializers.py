from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('photo', 'rating', 'text')


class FetchReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'activity', 'location', 'user', 'photo', 'created', 'updated', 'rating', 'text')
