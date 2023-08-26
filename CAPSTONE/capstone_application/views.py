from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . models import * 

# Create your views here.
# introduction to page
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "capstone_application/index.html")
    # Optional: Display globe of world as a heat map of lost pets/ homeless pets

    # display most recent post in cover page with sliding affect 

    #return render(request, "capstone_application/index.html")

def login_view(request):
    if request.method == "POST":
    #     # Get username
        username = request.POST.get("username")
    #     # Get password
        password = request.POST.get("password")

        user = authenticate(request, username=username, password= password)
        
        # If user object is returned, log in and route to index page:
        if user:
            login(request, user)
            return render(request, "capstone_application/user.html", {
                "message": "User was found!"
            })
        # Otherwise, return login page again with new context
        else:
            return render(request, "capstone_application/login.html", {
                "message": "User was NOT found!"
            })
    return render(request, "capstone_application/login.html")

def logout_view(request):
    logout(request)
    return render(request, "capstone_application/login.html", {
                "message": "Logged Out"
            })

def register(request):
    # Get username
    
    # Get password

    # Submit username and password to database

    # If succesful return index page

    # If not return register page again
    
    return render(request, "capstone_application/register.html")

def mercury(request):
    # choose mercury camera
    camera = 'mercury'
    return render(request,'capstone_application/mercury.html',{
        "camera" : camera,
    })

def venus(request):
    return render(request,'capstone_application/venus.html')

def earth(request):
    return render(request,'capstone_application/earth.html')

def mars(request):
    return render(request,'capstone_application/mars.html')

def jupiter(request):
    return render(request,'capstone_application/jupiter.html')

def saturn(request):
    return render(request,'capstone_application/saturn.html')

def uranus(request):
    return render(request,'capstone_application/uranus.html')

def neptune(request):
    return render(request,'capstone_application/neptune.html')
