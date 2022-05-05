from django.urls import path
from .views import FetchLocationView, CreateLocationView, DeleteLocationView, UpdateLocationView, FetchAllView 

urlpatterns = [
    path('<int:location_id>', FetchLocationView.as_view()),
    path('all', FetchAllView.as_view()),
    path('create', CreateLocationView.as_view()),
    path('delete/<int:location_id>', DeleteLocationView.as_view()),
    path('update/<int:location_id>', UpdateLocationView.as_view())
]
