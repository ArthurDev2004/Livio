from django.urls import path
from . import views

app_name = 'nationalities'

urlpatterns = [
    path('all', views.allNationalities, name="all_nationalities"),
    path('create', views.createNationalities, name='create')
]