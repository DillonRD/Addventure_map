from django.urls import path
from .views import FetchUsersView, CreateUserView, LoginUserView, DeleteUserView, LogoutUserView, UpdateUserView

urlpatterns = [
    path('users', FetchUsersView.as_view()),
    path('create', CreateUserView.as_view()),
    path('', LoginUserView.as_view()),
    path('delete', DeleteUserView.as_view()),
    path('logout', LogoutUserView.as_view()),
    path('update', UpdateUserView.as_view())
]
