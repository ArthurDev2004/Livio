from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def feature(request):
    return JsonResponse({'name' : 'Pet-Friendly'})