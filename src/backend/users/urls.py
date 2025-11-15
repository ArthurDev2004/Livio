from django.urls import path
from . import views

"""
Module Name: users.urls 
Date of Code: October 30, 2025
Description: Specifies the URL endpoints which will be used for each purpose, and the acompanying functions which will be used in response to the endpoint 
Important Functions:
Data Structures:
    urlpatterns - Django specific naming so it can be used by the main project folder to create all the endpoints
Important Functions: N/A
Algorithms: N/A
"""




app_name = "users"

urlpatterns = [
    path('all', views.getUser, name="get-user")
]