from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Blog home page!")


def about(request):
    a = 10+10
    return HttpResponse(f"About Page:{a}")