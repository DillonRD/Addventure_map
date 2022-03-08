from django.shortcuts import render
from rest_framework import generics, status
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .serializers import GetUserSerializer, GetAccountSerializer, GetReviewSerializer, GetLocationSerializer, GetActivitySerializer, GetPostSerializer, CreateActivitySerializer, CreateLocationSerializer, CreateUserSerializer, DeleteActivitySerializer, DeleteLocationSerializer, DeletePostSerializer, DeleteReviewSerializer, DeleteUserSerializer 
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response


class GetAccountView(APIView):
    serializer_class = GetLocationSerializer

    def get(self, request):
        #if self.request.session.get('session_token') is None:
        #    return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        print(self.request.session.get('user_id'))
        queryset = Location.objects.all()
        locations = GetLocationSerializer(queryset, many=True).data
        return Response(locations, status.HTTP_200_OK)

class GetLocationView(APIView):
    serializer_class = GetAccountSerializer

    def get(self, request):
        #if self.request.session.get('session_token') is None:
        #    return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        print(self.request.session.get('user_id'))
        queryset = User.objects.all()
        users = GetAccountSerializer(queryset, many=True).data
        return Response(users, status.HTTP_200_OK)
    
class GetUsersView(APIView):
    serializer_class = GetUserSerializer

    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        print(self.request.session.get('user_id'))
        queryset = User.objects.all()
        users = GetUserSerializer(queryset, many=True).data
        return Response(users, status.HTTP_200_OK)
    

# class DeleteUserView(APIView):
    
#     def delete(self, request, review_id):
#         #if self.request.session.get('session_token') is None:
#             #return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

#         try:
#             user = User.objects.get(id=review_id)
#         except User.DoesNotExist:
#             return Response("Review does not exist", status.HTTP_404_NOT_FOUND)

#         user.delete()
#         return Response("Review deleted", status.HTTP_200_OK)