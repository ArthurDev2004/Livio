from django.urls import path
from . import views

app_name = "market"

urlpatterns = [
    path("health/", views.health, name="health"),
    path("products/", views.products, name="products"),
    path("categories/", views.categories, name="categories"),
]
