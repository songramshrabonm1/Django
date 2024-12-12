from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("This is a httpResponse courses request")

def home(request):
    return HttpResponse("This is a Home page httpResponse first_app")
