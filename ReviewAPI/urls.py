from django.urls import path
from .views import FetchReviewsView, CreateReviewView, DeleteReviewView

urlpatterns = [
    path('', FetchReviewsView.as_view()),
    path('create', CreateReviewView.as_view()),
    path('delete/<int:review_id>', DeleteReviewView.as_view())
]
