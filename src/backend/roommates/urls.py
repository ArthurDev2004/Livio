from django.urls import path
from . import views # imports the views.py module from the current directory 

app_name = "roommates" # can be used later down the line if needed for resolving naming conflicts

urlpatterns = [
    path('greeting', views.greetThem, name="greeting"),
    path('current', views.currentUserRoommatePost, name='currrent_user_roommate_post'),
    path('current/interested', views.interestedRoommates, name='current_user_interested_roommates'), # returns the possible roommates that the currrent user is interested in
    path('create/', views.createRoommatePost, name="create_roommate_post"), 
    path('current/interested/add', views.addInterestedRoommate, name="add_interested_roommate")
]

