from django.db import models
from posts.models import Post
from features.models import Feature

class ApartmentPost(Post):
    
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=10)

    monthly_rent = models.DecimalField(max_digits=8, decimal_places=2)
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    square_feet = models.PositiveIntegerField(null=True, blank=True)

    features = models.ManyToManyField(Feature, blank=True)

    available_from = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.city}"