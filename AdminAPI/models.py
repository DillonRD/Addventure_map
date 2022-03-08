from django.db import models
from django.core.validators import MaxValueValidator

class Location(models.Model):
    discription = models.CharField(max_length=300)
    name = models.CharField(max_length=100, null=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zipcode = models.IntegerField(validators=[MaxValueValidator(99999)], null=True)
    altitude = models.IntegerField()
    
    
class Activity(models.Model):
    discription = models.CharField(max_length=300)
    name = models.CharField(max_length=100, null=True)
    approach = models.DecimalField(max_digits=5, decimal_places=2)
    altitude = models.IntegerField()
    height = models.IntegerField()
    difficulty = models.CharField(max_length=50)
    start_latitude = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)   
    finish_latitude = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    finish_longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)   
    location = models.ForeignKey(Location, related_name='activity_location', on_delete=models.CASCADE)
    
class Route(models.Model):
    discription = models.CharField(max_length=300)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    grade = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='Route_Images')
    

