from django.shortcuts import render
from rest_framework import generics, status
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .serializers import GetUserSerializer, GetAccountSerializer, GetReviewSerializer, GetLocationSerializer, GetActivitySerializer, GetPostSerializer, CreateActivitySerializer, CreateLocationSerializer, CreateUserSerializer, DeleteActivitySerializer, DeleteLocationSerializer, DeletePostSerializer, DeleteReviewSerializer, DeleteUserSerializer 
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class GetAccountView(APIView):
    serializer_class = GetAccountSerializer

    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        print(self.request.session.get('user_id'))
        queryset = User.objects.all()
        users = GetAccountSerializer(queryset, many=True).data
        return Response(users, status.HTTP_200_OK)
    

    
class DeleteUserView(APIView):
    serializer_class = DeleteUserSerializer

    def delete(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            user = User.objects.get(username=username)
            User.objects.filter(id=request.session.get('user_id'))
            user.delete()
            return Response("User deleted", status.HTTP_200_OK)


class GetUsersView(APIView):
    serializer_class = GetUserSerializer

    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        print(self.request.session.get('user_id'))
        queryset = User.objects.all()
        users = GetUserSerializer(queryset, many=True).data
        return Response(users, status.HTTP_200_OK)