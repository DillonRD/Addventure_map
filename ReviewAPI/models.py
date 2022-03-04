from django.db import models

# Create your models here.

class Review(models.Model):
    reviewId = models.IntegerField()
    userId = models.IntegerField()
    locationId = models.IntegerField()
    reviewImageId = models.IntegerField(null=True)
    datePost = models.DateField()
    reason = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits = 2,decimal_places=1)
