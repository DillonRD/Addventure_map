from django.urls import path
from .views import FetchReviewsByLocationView, CreateReviewView, DeleteReviewView, UpdateReviewView

urlpatterns = [
    path('name=<str:name>', FetchReviewsByLocationView.as_view()),
    path('create', CreateReviewView.as_view()),
    path('delete/<int:review_id>', DeleteReviewView.as_view()),
    path('update/<int:review_id>', UpdateReviewView.as_view())
]
