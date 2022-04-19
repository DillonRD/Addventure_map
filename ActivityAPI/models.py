from django.db import models
from LocationAPI.models import Location


class Activity(models.Model):
    description = models.CharField(max_length=300)
    name = models.CharField(max_length=100, null=True)
    approach = models.DecimalField(max_digits=5, decimal_places=2)
    altitude = models.IntegerField()
    height = models.IntegerField()
    difficulty = models.CharField(max_length=50)
    start_latitude = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    start_longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    finish_latitude = models.DecimalField(max_digits=12, decimal_places=6, default=0.0)
    finish_longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        db_table = "activity"
