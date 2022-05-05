from django.urls import path
from .views import *

urlpatterns = [
    path('name=<str:name>', FetchPostsByLocationView.as_view()),
    path('', GetPostsView.as_view()),
    path('<int:user_id>', GetPostView.as_view()),
    path('create', CreatePostView.as_view()),
    path('delete/<int:review_id>', DeletePostView.as_view()),
    path('update/<int:review_id>', UpdatePostView.as_view())
]
