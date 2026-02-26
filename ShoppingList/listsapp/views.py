from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from .models import User

# Create your views here.

def index(request):
    return render(request, "listsapp/index.html") 

def listpage(request):
    pass

def supermarketpage(request):
    pass

def productpage(request):
    pass

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "listsapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "listsapp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "listsapp/register.html", {
                "message": "Passwords must match."
            })
        is_supermarket = request.POST.get("is_supermarket") == "on"


        try:
            user = User.objects.create_user(username, email, password)
            user.is_supermarket = is_supermarket
            user.save()
        except IntegrityError:
            return render(request, "listsapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "listsapp/register.html")