from django.shortcuts import render
from rest_framework import generics, status
from .serializers import UserSerializer, CreateUserSerializer, AuthenticateUserSerializer, UpdateUserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
import bcrypt


# Create your views here.

class FetchUsersView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        print(self.request.session.get('user_id'))
        queryset = User.objects.all()
        users = UserSerializer(queryset, many=True).data
        return Response(users, status.HTTP_200_OK)


class DeleteUserView(APIView):
    serializer_class = AuthenticateUserSerializer

    def delete(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            user = User.objects.get(username=username)
            # User.objects.filter(id=request.session.get('user_id'))
            user.delete()
            return Response("User deleted", status.HTTP_200_OK)


class CreateUserView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            email = serializer.data.get('email')
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            confirmPassword = serializer.data.get('confirmPassword')

            # validate the fields

            if password != confirmPassword:
                return Response("Error: Passwords do not match", status.HTTP_400_BAD_REQUEST)

            queryset = User.objects.filter(username=username)
            if queryset.exists():
                return Response("Error: username already taken", status.HTTP_400_BAD_REQUEST)
            else:
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                user = User(email=email, username=username, password=hashed_password.decode())
                user.save()
                self.request.session['user_id'] = user.pk
                return Response(UserSerializer(user).data, status.HTTP_201_CREATED)


class LoginUserView(APIView):
    serializer_class = AuthenticateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')

            queryset = User.objects.filter(username=username)
            if queryset.exists():
                if bcrypt.checkpw(password.encode('utf-8'), queryset[0].password.encode('utf-8')):

                    # if login is correct create a session
                    if self.request.session.get('session_token') is None:
                        self.request.session.create()

                    # create a session variable that stores user id and session token
                    self.request.session['user_id'] = queryset[0].pk
                    self.request.session['session_token'] = self.request.session.session_key

                    return Response("correct login", status.HTTP_200_OK)

            # if any login credentials were incorrect error is returned
            return Response("Error: incorrect login", status.HTTP_401_UNAUTHORIZED)


class LogoutUserView(APIView):

    def post(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        self.request.session.flush()
        return Response("successful logout", status.HTTP_200_OK)


class UpdateUserView(APIView):
    serializer_class = UpdateUserSerializer

    def put(self, request):
        if self.request.session.get('session_token') is None and self.request.session.get('user_id') is None:
            return Response("Error: You shouldn't be here", status.HTTP_401_UNAUTHORIZED)

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            firstname = serializer.data.get('firstname')
            lastname = serializer.data.get('lastname')
            dateOfBirth = serializer.data.get('dateOfBirth')
            phone = serializer.data.get('phone')
            email = serializer.data.get('email')
            address = serializer.data.get('address')
            city = serializer.data.get('city')
            zipcode = serializer.data.get('zipcode')
            latitude = serializer.data.get('latitude')
            longitude = serializer.data.get('longitude')

            # after creating username and password more information is asked for in the next page
            # id and isAdmin cannot be updated by user
            # user has to fill out this if they want the cool features
            # validate the fields

            queryset = User.objects.filter(id=request.session.get('user_id'))
            user = queryset[0]
            fieldsToUpdate = []

            if username != user.username:
                if username is not None:
                    user.username = username
                    fieldsToUpdate.append('username')
            if password != user.password:
                if password is not None:
                    user.password = password
                    fieldsToUpdate.append('password')
            if firstname != user.firstname:
                user.firstname = firstname
                fieldsToUpdate.append('firstname')
            if lastname != user.lastname:
                user.lastname = lastname
                fieldsToUpdate.append('lastname')
            if dateOfBirth != user.dateOfBirth:
                user.dateOfBirth = dateOfBirth
                fieldsToUpdate.append('dateOfBirth')
            if phone != user.phone:
                user.phone = phone
                fieldsToUpdate.append('phone')
            if email != user.email:
                user.email = email
                fieldsToUpdate.append('email')
            if address != user.address:
                user.address = address
                fieldsToUpdate.append('address')
            if city != user.city:
                user.city = city
                fieldsToUpdate.append('city')
            if zipcode != user.zipcode:
                user.zipcode = zipcode
                fieldsToUpdate.append('zipcode')
            if latitude != user.latitude:
                user.latitude = latitude
                fieldsToUpdate.append('latitude')
            if longitude != user.longitude:
                user.longitude = longitude
                fieldsToUpdate.append('longitude')

            user.save(update_fields=fieldsToUpdate)
            return Response("Successfully Updated", status.HTTP_200_OK)