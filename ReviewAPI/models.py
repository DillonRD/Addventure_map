from django.db import models


# Create your models here.

class Review(models.Model):
    review_id = models.IntegerField()
    user_id = models.IntegerField()
    location_id = models.IntegerField()
    review_image_id = models.IntegerField(null=True)
    date_post = models.DateField()
    reason = models.CharField(max_length=300)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
