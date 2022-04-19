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

        queryset = Review.objects.filter(user=user_id)
        reviews = FetchReviewSerializer(queryset, many=True).data
        return Response(reviews, status.HTTP_200_OK)


class CreateReviewView(APIView):
    serializer_class = ReviewSerializer

    def post(self, request):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            activity = self.request.session.get('activity')
            location = self.request.session.get('location')
            user = self.request.session.get('user')
            photo = serializer.data.get('photo')
            rating = serializer.data.get('rating')
            text = serializer.data.get('text')

            review = Review(activity=activity, location=location, user=user, photo=photo, rating=rating, text=text)
            review.save()
            return Response(FetchReviewSerializer(review).data, status.HTTP_201_CREATED)


class DeleteReviewView(APIView):

    def delete(self, request, review_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        try:
            review = Review.objects.get(id=review_id)
        except Review.DoesNotExist:
            return Response("Review does not exist", status.HTTP_404_NOT_FOUND)

        review.delete()
        return Response("Review deleted", status.HTTP_200_OK)


class UpdateReviewView(APIView):
    serializer_class = ReviewSerializer

    def put(self, request, review_id):
        #if self.request.session.get('session_token') is None:
            #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            photo = serializer.data.get('photo')
            rating = serializer.data.get('rating')
            text = serializer.data.get('text')

            review = Review.objects.get(id=review_id)
            fieldsToUpdate = []

            if photo != review.photo:
                review.photo = photo
                fieldsToUpdate.append('photo')
            if rating != review.rating:
                review.rating = rating
                fieldsToUpdate.append('rating')
            if text != review.text:
                review.text = text
                fieldsToUpdate.append('text')

            review.save(update_fields=fieldsToUpdate)
            return Response("Review updated", status.HTTP_200_OK)
