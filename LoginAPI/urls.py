from django.urls import path
from .views import RegisterView, LoginView, FetchUserView, LogoutView, FetchUsersView, DeleteView, UpdateView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', FetchUserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('users', FetchUsersView.as_view()),
    path('delete', DeleteView.as_view()),
    path('update', UpdateView.as_view())
]