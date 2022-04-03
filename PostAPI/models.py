from django.db import models
from LoginAPI.models import User
from ActivityAPI.models import Activity
from LocationAPI.models import Location


class Post(models.Model):
    activity = models.ForeignKey(Activity, related_name='activity_post', on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name='location_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_post', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Post_Images')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)
    likes = models.IntegerField(default=0)
    text = models.CharField(max_length=300, default='')

class Route(models.Model):
    discription = models.CharField(max_length=300)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    grade = models.CharField(max_length=16)
    photo = models.ImageField(upload_to='Route_Images')