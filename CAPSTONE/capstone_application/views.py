from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from . models import * 

# Create your views here.
# introduction to page
def index(request):
    # if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse("login"))
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
