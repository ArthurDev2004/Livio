from django.urls import path
from . import views

app_name = "features"

urlpatterns = [
    path('feature', views.feature, name='feature'),
    path('post', views.postfeature, name='post'),
    path('newfeature', views.createFeature, name='create'),
    path('new', views.new, name='new')
]