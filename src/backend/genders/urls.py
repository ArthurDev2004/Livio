from django.urls import path
from . import views

app_name = 'genders'

urlpatterns = [
    path('create', views.createGender, name="create_gender")
]