from django.urls import path
from .views import GetAccountView, GetUsersView
from ReviewAPI.views import DeleteReviewView
urlpatterns = [
    path('accounts', GetAccountView.as_view()),
    path('users', GetUsersView.as_view()),
    path('review/<int:review_id>', DeleteReviewView.as_view()),
]
