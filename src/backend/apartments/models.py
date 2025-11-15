from django.db import models
from posts.models import Post
from features.models import Feature

"""
Module: apartments.models
Date: November 1, 2025
Programmer: Arrshan Saravanabavanandam

Description:
    Contains the ApartmentPost model, which represents an apartment listing.
    This class extends the abstract Post base class and adds fields specific
    to rental properties (rent, bedrooms, address, square footage, etc.).
"""



class ApartmentPost(Post):

    """
    Class: ApartmentPost
    Date: 2025-11-14
    Programmer: Arrshan Saravanabavanandam

    Description:
        Extends the abstract Post class to represent an apartment listing in the Livio application.
        Includes rental information such as rent, bedrooms, bathrooms, square footage, and availability.

    Important Fields:
        address (str): Street address of the apartment.
        city (str): City in which the apartment is located.
        monthly_rent (Decimal): Monthly cost of rent.
        features (ManyToMany[Feature]): Amenity tags such as A/C, Parking, Laundry.

    Algorithms / Notes:
        No special algorithms used here — relies on Django ORM to map the model to the database.
    """

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