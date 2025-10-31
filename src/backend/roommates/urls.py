from django.urls import path
from . import views # imports the views.py module from the current directory 

app_name = "roomates" # can be used later down the line if needed for resolving naming conflicts

urlpatterns = [
    path('greeting', views.greetThem, name="greeting"),
    path('current', views.currentUserRoommatePost, name='currrent_user_roommate_post')
]

