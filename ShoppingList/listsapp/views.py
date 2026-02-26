from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Product, List, PriceMkt
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    supermarkets = User.objects.all().filter(is_supermarket=True)
    products = Product.objects.all().order_by("name")
    listuser = None
    if request.user.is_authenticated :
        listuser = List.objects.filter(user=request.user)
    return render(request, "listsapp/index.html",{
        "supermarkets": supermarkets,
        "list": listuser,
        "products": products
    }) 

@login_required
def listpage(request, list_id):
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    products = list_obj.products.all().order_by("name")

    return render(request, "listsapp/listpage.html", {
        "list": list_obj,
        "products": products
    })

@login_required
def userpage(request):
    lists = List.objects.filter(user=request.user)
    return render(request, "listsapp/userpage.html", {
        "lists": lists
    })

def supermarketpage(request, supermarket_id):
    supermarket = get_object_or_404(
        User,
        id=supermarket_id,
        is_supermarket=True
    )
    prices = PriceMkt.objects.filter(supermarket=supermarket).select_related("product")
    return render(request, "listsapp/supermarketpage.html", {
        "supermarket": supermarket,
        "prices": prices
    })

def productpage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "listsapp/productpage.html", {
        "product": product
    })

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