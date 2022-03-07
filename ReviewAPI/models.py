from django.db import models
from LoginAPI.models import User
from AdminAPI.models import Activity, Location

class Review(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Review_Images')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    text = models.CharField(max_length=300)

    class Meta:
        db_table = "review"
