from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    photo = serializers.ImageField(
        max_length=None, use_url=True,
    )
    class Meta:
        model = Review
        fields = ('activity', 'location', 'user', 'photo', 'created', 'updated', 'rating', 'text')


class FetchReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'activity', 'location', 'user', 'photo', 'created', 'updated', 'rating', 'text')
