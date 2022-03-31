from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'isAdmin', 'isVerified', 'username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email',
                  'address', 'city', 'zipcode', 'latitude', 'longitude')


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'firstname', 'lastname', 'dateOfBirth', 'phone', 'email', 'address', 'city',
                  'zipcode', 'latitude', 'longitude')


class AuthenticateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'confirmPassword')