from django.urls import path
from .views import GetUsersView, GetLocationView
from ReviewAPI.views import DeleteReviewView
from UserAPI.views import GetAccountView

urlpatterns = [
    path('account', GetAccountView.as_view()),
    path('user', GetUsersView.as_view()),
    path('location', GetLocationView.as_view()),
    path('review/<int:review_id>', DeleteReviewView.as_view()),
]
