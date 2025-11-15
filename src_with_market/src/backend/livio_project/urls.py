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

def home(request):
    return render(request, "home_page.html")

def login_view(request):
    return render(request, "login_page.html")

def signup(request):
    return render(request, "signup_page.html")

def marketplace(request):
    return render(request, "marketplace.html")

urlpatterns = [
    path('api/market/', include('market.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('marketplace/', marketplace, name='marketplace'),  
    
    path('', include("roommates.urls")),
    path('features/', include('features.urls'))
]

# added all of the urls from the roommates app urls.py to the main one, so it is able to go to the proper place