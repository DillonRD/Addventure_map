from rest_framework import status
from .serializers import ReviewSerializer, FetchReviewSerializer
from .models import Review
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class FetchReviewsView(APIView):
    serializer_class = ReviewSerializer

    def get(self, request, user_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        queryset = Review.objects.filter(user_id=user_id)
        reviews = FetchReviewSerializer(queryset, many=True).data
        return Response(reviews, status.HTTP_200_OK)


class CreateReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user_id = serializer.data.get('user_id')
            location_id = serializer.data.get('location_id')
            review_image_id = serializer.data.get('review_image_id')
            date_post = serializer.data.get('date_post')
            reason = serializer.data.get('reason')
            rating = serializer.data.get('rating')

            review = Review(user_id=user_id, location_id=location_id, review_image_id=review_image_id, date_post=date_post, reason=reason, rating=rating)
            review.save()
            return Response(ReviewSerializer(review).data, status.HTTP_201_CREATED)


class DeleteReviewView(APIView):

    def delete(self, request, review_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            review = Review.objects.get(review_id=review_id)
        except Review.DoesNotExist:
            return Response("Review does not exist", status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response("Review deleted", status.HTTP_200_OK)
