from django.urls import path
from .views import FetchReviewsView, CreateReviewView

urlpatterns = [
    path('', FetchReviewsView.as_view()),
    path('create', CreateReviewView.as_view())
]
