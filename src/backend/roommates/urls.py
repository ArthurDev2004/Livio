from django.urls import path
from . import views # imports the views.py module from the current directory 

"""
Module Name: roommates.urls 
Date of Code: October 15, 2025 - November 10, 2025
Description: Specifies the URL endpoints which will be used for each purpose, and the acompanying functions which will be used in response to the endpoint 
Important Functions:
Data Structures:
    urlpatterns - Django specific naming so it can be used by the main project folder to create all the endpoints
Important Functions: N/A
Algorithms: N/A
"""


app_name = "roommates" # can be used later down the line if needed for resolving naming conflicts

urlpatterns = [
    path('greeting', views.greetThem, name="greeting"),
    path('current', views.currentUserRoommatePost, name='currrent_user_roommate_post'),
    path('current/interested', views.interestedRoommates, name='current_user_interested_roommates'), # returns the possible roommates that the currrent user is interested in
    path('create/', views.createRoommatePost, name="create_roommate_post"), 
    path('current/interested/add', views.addInterestedRoommate, name="add_interested_roommate"),
    path("update/", views.editRoommatePost, name="update_roommate_post"),
    path('', views.pagination, name="get_page")
]

