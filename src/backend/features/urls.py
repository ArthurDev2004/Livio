from django.urls import path
from . import views

app_name = "features"

urlpatterns = [
    path('feature', views.feature, name='feature')
]