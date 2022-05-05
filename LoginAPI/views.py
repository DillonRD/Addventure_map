from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer, UpdateUserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime


# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='JWT', value=token, httponly=True, samesite='None', secure=True)
        response.data = {
            'JWT': token
        }
        return response


class FetchUserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('JWT')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UpdateUserSerializer(user)
        return Response(serializer.data)


class FetchUsersView(APIView):
    def get(self, request):
        """
        token = request.COOKIES.get('JWT')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        """
        users = User.objects.all()
        serializer = UpdateUserSerializer(users, many=True)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('JWT', samesite='None')
        response.data = {
            'message': 'success'
        }
        return response


class DeleteView(APIView):
    def delete(self, request):
        """
        token = request.COOKIES.get('JWT')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        """
        email = request.data['email']
        user = User.objects.filter(email=email).first()
        user.delete()
        return Response("User deleted", status.HTTP_200_OK)


class UpdateView(APIView):
    def put(self, request):
        token = request.COOKIES.get('JWT')
        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        email = request.data['email']
        password = request.data['password']
        firstname = request.data['firstname']
        lastname = request.data['lastname']
        dateOfBirth = request.data['dateOfBirth']
        phone = request.data['phone']
        address = request.data['address']
        city = request.data['city']
        zipcode = request.data['zipcode']

        user = User.objects.filter(id=payload['id']).first()
        fieldsToUpdate = []

        if user.email != email:
            user.email = email
            fieldsToUpdate.append('email')
        if user.password != password:
            if password != "":
                print(password)
                #user.password = password
                #fieldsToUpdate.append('password')
        if user.firstname != firstname:
            user.firstname = firstname
            fieldsToUpdate.append('firstname')
        if user.lastname != lastname:
            user.lastname = lastname
            fieldsToUpdate.append('lastname')
        if user.dateOfBirth != dateOfBirth:
            user.dateOfBirth = dateOfBirth
            fieldsToUpdate.append('dateOfBirth')
        if user.phone != phone:
            user.phone = phone
            fieldsToUpdate.append('phone')
        if user.address != address:
            user.address = address
            fieldsToUpdate.append('address')
        if user.city != city:
            user.city = city
            fieldsToUpdate.append('city')
        if user.zipcode != zipcode:
            user.zipcode = zipcode
            fieldsToUpdate.append('zipcode')

        user.save(update_fields=fieldsToUpdate)
        return Response("Successfully Updated", status.HTTP_200_OK)
