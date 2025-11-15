from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

"""
Module Name: users.views
Date of Code: October 30, 2025
Programmer's Name: Arthur Lazaryan
Description: Has the functions which pertain the endpoints in regards to the User class
Important Functions: 
    getUser - returns the specific user making the endpoint request; does so with the JWT Token used 
Data Structures:
    api_view - Django REST Framework decorator, which allows to specify the HTTP method which the endpoint via this function can be used with 

    permission_classes - Django REST framework decorator, which specifies which authentication/authorization level is needed to access the endpoint via the function
Algorithms: N/A
"""

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUser(request):
    """
    Function Name: getUser
    Date of Code: October 30, 2025
    Description: Returns the current user which is logged in 
        Input:
            request - Django REST framework specific implementation which has all the data from the HTTP request header and body, which includes the JWT token used to identify the user
        Output:
            None
    Data Structures: N/A
    Algorithms: N/A
    """
    pass