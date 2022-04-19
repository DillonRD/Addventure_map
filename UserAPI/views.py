from django.shortcuts import render
from rest_framework import generics, status
from .serializers import GetAccountSerializer, UpdateUserSerializer, DeleteUserSerializer
from LoginAPI.models import User
from rest_framework.views import APIView
from rest_framework.response import Response 


class GetAccountView(APIView):
    serializer_class = GetAccountSerializer

    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        #print(self.request.session.get('user_id'))
        queryset = User.objects.filter(id=request.session.get('user_id'))
        
        Account = GetAccountSerializer(queryset, many=True).data
        return Response(Account, status.HTTP_200_OK)
    
class GetOtherAccountView(APIView):
    serializer_class = GetAccountSerializer
    
    def get(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)

        #print(self.request.session.get('user_id'))
        queryset = User.objects.all()
        
        Account = GetAccountSerializer(queryset, many=True).data
        return Response(Account, status.HTTP_200_OK)

class DeleteUserView(APIView):
    serializer_class = DeleteUserSerializer


    def delete(self, request):
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            #username = serializer.data.get('username')
            #user = User.objects.get(username=username)
            user = User.objects.filter(id=request.session.get('user_id'))
            user.delete()
            return Response("User deleted", status.HTTP_200_OK)
        else:    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
                if firstname is not None:
                    user.firstname = firstname
                    fieldsToUpdate.append('firstname')
            if lastname != user.lastname:
                if lastname is not None:
                    user.lastname = lastname
                    fieldsToUpdate.append('lastname')
            if dateOfBirth != user.dateOfBirth:
                if dateOfBirth is not None:
                    user.dateOfBirth = dateOfBirth
                    fieldsToUpdate.append('dateOfBirth')
            if phone != user.phone:
                if phone is not None:
                    user.phone = phone
                    fieldsToUpdate.append('phone')
            if email != user.email:
                if email is not None:
                    user.email = email
                    fieldsToUpdate.append('email')
            if address != user.address:
                if address is not None:
                    user.address = address
                    fieldsToUpdate.append('address')
            if city != user.city:
                if city is not None:
                    user.city = city
                    fieldsToUpdate.append('city')
            if zipcode != user.zipcode:
                if zipcode is not None:
                    user.zipcode = zipcode
                    fieldsToUpdate.append('zipcode')
            if latitude != user.latitude:
                if latitude is not None:
                    user.latitude = latitude
                    fieldsToUpdate.append('latitude')
            if longitude != user.longitude:
                if longitude is not None:
                    user.longitude = longitude
                    fieldsToUpdate.append('longitude')

            user.save(update_fields=fieldsToUpdate)
            return Response("Successfully Updated", status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
