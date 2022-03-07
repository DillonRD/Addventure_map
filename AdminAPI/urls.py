from django.urls import path
from .views import GetAccountView, GetUsersView

urlpatterns = [
    path('accounts', GetAccountView.as_view()),
    path('users', GetUsersView.as_view()),
]
