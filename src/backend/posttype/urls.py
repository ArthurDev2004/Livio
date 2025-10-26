from django.urls import path
from . import views

app_name = 'posttype'

urlpatterns = [
    path('create', views.createPostType, name="create_post_type"),
    path('all', views.getPostTypes, name="all")
]