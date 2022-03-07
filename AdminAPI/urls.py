from django.urls import path
from .views import GetAccountView

urlpatterns = [
    path('accounts', GetAccountView.as_view()),
]