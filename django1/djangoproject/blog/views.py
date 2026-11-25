from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to the blog home Page!")


def about(request):
    a= 10+50
    return HttpResponse(f"About page: {a}")