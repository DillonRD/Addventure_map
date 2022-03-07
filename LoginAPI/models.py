from django.db import models
from django.core.validators import MaxValueValidator


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
    isAdmin = models.BooleanField(default=False , null=False)
    phone = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(validators=[MaxValueValidator(99999)], null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
