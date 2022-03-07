from django.urls import path
from .views import FetchReviewsView, CreateReviewView, DeleteReviewView

urlpatterns = [
    path('<int:user_id>', FetchReviewsView.as_view()),
    path('create', CreateReviewView.as_view()),
    path('delete', DeleteReviewView.as_view())
]
