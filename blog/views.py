from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Blog Home Page - It Works!")

def about(request):
    return HttpResponse("About Page - Learn more about us here!")
