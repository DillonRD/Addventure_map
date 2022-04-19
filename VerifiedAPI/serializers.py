from rest_framework import serializers
from LoginAPI.models import User


class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'isVerified')



