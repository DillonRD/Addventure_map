from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('reviewId', 'userId', 'locationId', 'reviewImageId', 'datePost', 'reason', 'rating')

class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('userId', 'locationId', 'reviewImageId', 'datePost', 'reason', 'rating')
