from django.urls import path
from .views import GetAccountView, DeleteUserView,UpdateUserView

urlpatterns = [
    path('', GetAccountView.as_view()),
    path('delete', DeleteUserView.as_view()),
    path('update', UpdateUserView.as_view()),
]
