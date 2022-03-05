from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('review_id', 'user_id', 'location_id', 'review_image_id', 'date_post', 'reason', 'rating')


class UpdateReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user_id', 'location_id', 'review_image_id', 'date_post', 'reason', 'rating')
