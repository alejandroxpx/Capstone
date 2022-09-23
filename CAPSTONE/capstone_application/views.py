from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# introduction to page
def index(request):
    return render(request, "capstone_application/index.html")

def lost_pets(request):
    return HttpResponse("Lost_pets Page")   

def login(request):
    return HttpResponse("logging in to page")

def logout(request):
    return HttpResponse("logging out of page")

def register(request):
    return HttpResponse("registering to page")
 