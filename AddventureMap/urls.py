"""AddventureMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('UserAPI.urls')),
    path('verify/', include('VerifiedAPI.urls')),
    path('', include('LoginAPI.urls')),
    path('review/', include('ReviewAPI.urls')),
    path('post/', include('PostAPI.urls')),
    path('location/', include('LocationAPI.urls')),
    path('activity/', include('ActivityAPI.urls'))
]
