from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def greetThem(request):
    greeting = {'greeting' : "Hello, how are you?"}

    return JsonResponse(greeting)

def personalGreeting(request, name):
    greeting = {'greeting' : f"Hello {name}, how are you?"}

    return JsonResponse(greeting) # returns a JSON to the frontend, which can be very useful
