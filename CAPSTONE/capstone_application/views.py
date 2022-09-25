from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

# introduction to page
def index(request):
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

def login(request):
    # Get username

    # Get password

    # if found in database, login and return home page

    # else, return error and reload login page

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
 