from django.urls import path
from .views import GetAccountView, GetUsersView, GetLocationView
from ReviewAPI.views import DeleteReviewView
urlpatterns = [
    path('account', GetAccountView.as_view()),
    path('user', GetUsersView.as_view()),
    path('location', GetLocationView.as_view()),
    path('review/<int:review_id>', DeleteReviewView.as_view()),
]
