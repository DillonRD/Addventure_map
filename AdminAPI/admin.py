from django.contrib import admin
from .models import Activity, Location, Route
from ReviewAPI.models import Review
from LoginAPI.models import User
from PostAPI.models import Post

admin.site.register(User)
admin.site.register(Activity)
admin.site.register(Location)
admin.site.register(Post)
admin.site.register(Route)
admin.site.register(Review)

