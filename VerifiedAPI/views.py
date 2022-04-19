
from django.shortcuts import redirect, render
from django.contrib import messages
from rest_framework import generics, status
from .serializers import VerifySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from LoginAPI.models import User
import bcrypt
from .send_mail import send_email


class VerifyUsersView(APIView):
    
    serializer_class = VerifySerializer
    
    def put(self, request):
        
        if self.request.session.get('session_token') is None:
            return Response("Error: No session token", status.HTTP_401_UNAUTHORIZED)
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            email = serializer.data.get('email')

            queryset = User.objects.filter(username=username)

            if queryset.exists():
                if bcrypt.checkpw(password.encode('utf-8'), queryset[0].password.encode('utf-8')):
                    
                    # if login is correct check if email exsist
                    if email is not None:
                        user = queryset[0]
                        fieldsToUpdate = []
                        #  check if email
                        if email != user.email:
                            user.email = email
                            fieldsToUpdate.append('email')
                            
                        user.save(update_fields=fieldsToUpdate)
                        
                        send_email(user, request)

                        return Response("verified", status.HTTP_200_OK)
                    else:
                        return Response("Error: email not found", status.HTTP_401_UNAUTHORIZED)
            return Response("Error: user not found", status.HTTP_401_UNAUTHORIZED)


    