from django.urls import path
from .views import VerifyUsersView
from .send_mail import verify_user

urlpatterns = [ 
    path('', VerifyUsersView.as_view()),
    path('<uidb64>/<token>', verify_user, name='verify')
   
]
