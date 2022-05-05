from django.urls import path
from .views import FetchActivityView, CreateActivityView, DeleteActivityView, UpdateActivityView,\
    FetchActivityByLocationView

urlpatterns = [
    path('<int:activity_id>', FetchActivityView.as_view()),
    path('name=<str:name>', FetchActivityByLocationView.as_view()),
    path('create', CreateActivityView.as_view()),
    path('delete/<int:activity_id>', DeleteActivityView.as_view()),
    path('update/<int:activity_id>', UpdateActivityView.as_view())
]
