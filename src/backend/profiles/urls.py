from django.urls import path
from . import views 


app_name = 'profiles'


urlpatterns = [
    path('profile', views.createProfile, name="create_profile"), # the route to create the profile 
    path('all', views.getProfile, name="get_profiles"),
    path('current', views.getCurrentUserProfile, name='current_profile')
]