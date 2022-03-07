from django.contrib import admin
from .models import User, Activity, Location, Post, Route
from ReviewAPI.models import Review

admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Route)
admin.site.register(Review)


# Register your models here.
