from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('all', views.getUser, name="get-user")
]