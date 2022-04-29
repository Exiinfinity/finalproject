"""finalproject URL Configuration

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
from .views import home, register,plantmanage
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),    
    path('users/', include('users.urls')), # users>urls.py에서 관리할거야
    path('', home),
    path('register/', register),
    path('main/', views.main, name="main"),
    path('plantinfo/', views.plantinfo, name="plantinfo"),
    path('plantmanage/', views.plantmanage, name="plantmanage"),
    path('plantrecog/', views.plantrecog, name="plantrecog"),
    path('plantdisease/', views.plantdisease, name="plantdisease"),
    path('search/', include('search_app.urls')),
    path('accounts/login', include('allauth.urls')),
    path('accounts/signup', include('allauth.urls')),
]