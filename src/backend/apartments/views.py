from django.shortcuts import render
from .models import ApartmentPost

"""
Module: apartments.views
Date: 2025-11-14
Programmer: Arrshan Saravanabavanandam

Description:
    This module defines the view functions for the Apartments app. These views
    act as the controller layer in the Django MVC/MVT pattern. They retrieve
    ApartmentPost objects from the database and render them using HTML templates.

Design Patterns:
    - MVC / MVT: This module provides the "View" layer, receiving HTTP requests,
      calling the model layer (ApartmentPost), and returning rendered templates.
"""

def apartment_list_view(request):
    """
    Function: apartment_list_view
    Date: 2025-11-14
    Programmer: Arrshan Saravanabavanandam

    Description:
        Handles requests to display a list of active apartment listings.
        Fetches ApartmentPost objects from the database and passes them
        to a Django template for rendering.

    Inputs:
        request (HttpRequest):
            The incoming HTTP request object.

    Returns:
        HttpResponse:
            An HTML page rendered from the 'apartments/list.html' template,
            containing a list of apartment posts.

    Algorithm:
        1. Query all ApartmentPost objects where is_active=True.
        2. Use select_related and prefetch_related to optimize database access
           for the related profile and features.
        3. Build a context dictionary and pass it to the render() function.
    """

    apartments = (
        ApartmentPost.objects
        .filter(is_active=True)
        .select_related('profile')
        .prefetch_related('features')
    )

    context = {
        "apartments": apartments,
    }

    return render(request, "apartments/list.html", context)