"""
URL configuration for livio_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return render(request, "home_page.html")

def login_view(request):
    return render(request, "login_page.html")

def signup(request):
    return render(request, "signup_page.html")

def apartment (request):
    return render(request, "apartment_page.html")

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('apartments/', apartment, name='apartment'),
    path('users/', include('users.urls')),
    path('profiles/', include('profiles.urls')),
    path('roommates/', include('roommates.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name="jwt"),
    path('api/token/refresh/', TokenRefreshView.as_view(), name="jwt_refresh"),
    path('', include("roommates.urls")),
    path('features/', include('features.urls'))
]

# added all of the urls from the roommates app urls.py to the main one, so it is able to go to the proper place