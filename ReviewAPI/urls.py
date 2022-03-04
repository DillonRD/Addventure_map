from django.urls import path
from .views import FetchUsersView, CreateUserView, LoginUserView, DeleteUserView, LogoutUserView, UpdateUserView

urlpatterns = [
    path('reviews', FetchReviewsView.as_view()),
    path('create', CreateReviewView.as_view()),
]
