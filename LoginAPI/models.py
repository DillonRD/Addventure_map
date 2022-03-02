from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    confirmPassword = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    dateOfBirth = models.DateField(null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=30, null=True)
