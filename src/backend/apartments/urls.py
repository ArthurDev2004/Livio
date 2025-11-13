from django.urls import path
from . import views

app_name = "apartments"

urlpatterns = [
    path('all', views.getFeatures)
]