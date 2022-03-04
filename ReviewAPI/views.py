from django.shortcuts import render
from rest_framework import status
from .serializers import ReviewSerializer, UpdateReviewSerializer
from .models import Review
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class FetchReviewsView(APIView):
    serializer_class = ReviewSerializer

    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        queryset = Review.objects.all()
        reviews = ReviewSerializer(queryset, many=True).data
        return Response(reviews, status.HTTP_200_OK)

class CreateReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            reviewId = serializer.data.get('reviewId')
            userId = serializer.data.get('userId')
            locationId = serializer.data.get('locationId')
            reviewImageId = serializer.data.get('reviewImageId')
            datePost = serializer.data.get('datePost')
            reason = serializer.data.get('reason')
            rating = serializer.data.get('rating')

            review = Review(reviewId=reviewId, userId=userId, locationId=locationId, reviewImageId=reviewImageId, datePost=datePost, reason=reason, rating=rating)
            review.save()
            return Response(ReviewSerializer(review).data, status.HTTP_201_CREATED)
