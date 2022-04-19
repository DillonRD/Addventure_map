from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.CharField(max_length=30, null=True, unique=True)
    password = models.CharField(max_length=100, null=True)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    dateOfBirth = models.DateField(null=True)
    phone = models.CharField(max_length=15, null=True)
    isAdmin = models.BooleanField(default=False, null=False)
    isVerified = models.BooleanField(default=False, null=False)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(validators=[MaxValueValidator(99999)], null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []