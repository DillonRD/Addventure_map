from django.urls import path
from .views import FetchReviewsView, CreateReviewView, DeleteReviewView, UpdateReviewView

urlpatterns = [
    path('<int:user_id>', FetchReviewsView.as_view()),
    path('create', CreateReviewView.as_view()),
    path('delete/<int:review_id>', DeleteReviewView.as_view()),
    path('update/<int:review_id>', UpdateReviewView.as_view())
]
