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

def lost_pets(request):
    # Get pet information

    # If already in database return error

    # else submit pet information into database

    # If lost display lost page

    # If homeless display homeless page


    return HttpResponse("Lost_pets Page")   

def login_view(request):
    if request.method == "POST":
        # Get username
        username = request.POST["username"]
        # Get password
        password = request.POST["password"]
        user = User.objects.get(username=username, password=password)
        # if found in database, login and return home page
        # user = authenticate(request, username=username,password=password)
        if user:
            # login(request, user)
            return HttpResponse("worked")
        # else, return error and reload login page
        else:
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
 