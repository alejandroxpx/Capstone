from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import * 

# Create your views here.

# introduction to page
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    # Optional: Display globe of world as a heat map of lost pets/ homeless pets

    # display most recent post in cover page with sliding affect 

    return render(request, "capstone_application/index.html")

def login_view(request):
    if request.method == "POST":
        # Get username
        username = request.POST["username"]
        # Get password
        password = request.POST["password"]
        
        # if found in database, login and return home page
        try:
            (User.objects.get(username=username, password=password))
            # login(request, user)
            return render(request,"capstone_application/home.html",{
                "message":"Hello, Alex!"
            })
        # return error and reload login page
        except:
            return render(request, "capstone_application/login.html",{
                "message":"Invalid credentials"
            })
    return render(request, "capstone_application/login.html")

def logout(request):
        return render(request, "capstone_application/index.html")

def register(request):
    # Get username
    
    # Get password

    # Submit username and password to database

    # If succesful return index page

    # If not return register page again
    
    return render(request, "capstone_application/register.html")
 
def home(request):
    return render(request, "capstone_application/home.html")
 
def homeless(request):
    return render(request, "capstone_application/homeless.html")

def stories(request):
    return render(request, "capstone_application/stories.html")

def lost(request):
    if request.method == "POST":
        # Get pet information
        name = request.POST["name"]
        location = request.POST["location"]
        age = request.POST["age"]
        size = request.POST["size"]
        image = request.POST["image"]
        breed = request.POST["breed"]

    # If already in database return error

    # else submit pet information into database

    # If lost display lost page

    # If homeless display homeless page

    return render(request, "capstone_application/lost.html")