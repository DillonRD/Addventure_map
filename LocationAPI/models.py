from django.db import models


class Location(models.Model):
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    altitude = models.IntegerField()

    class Meta:
        db_table = "location"
