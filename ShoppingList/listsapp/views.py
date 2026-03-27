import json

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse
from django.db import IntegrityError
from .models import User, Product, List, PriceMkt
from django.shortcuts import get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse



def index(request):
    supermarkets = User.objects.filter(is_supermarket=True)  
    product_list = Product.objects.all().order_by("name")
    
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        html = render_to_string("listsapp/includes/product_list_partial.html", {'products': products}, request=request)
        return JsonResponse({'html': html})

    listuser = None
    if request.user.is_authenticated and not request.user.is_supermarket:
        listuser = List.objects.filter(user=request.user)

    return render(request, "listsapp/index.html", {
        "supermarkets": supermarkets,
        "list": listuser,
        "products": products
    })
    
@login_required
def listpage(request, list_id):
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        if product_id:
            product = get_object_or_404(Product, id=product_id)
            if product not in list_obj.products.all():
                list_obj.products.add(product)
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({
                        "success": True,
                        "id": product.id,
                        "name": product.name,
                        "unity": product.unity
                    })
      
        return redirect("listpage", list_id=list_id)
    products_in_list = list_obj.products.all().order_by("name")
    all_products = Product.objects.exclude(id__in=products_in_list).order_by("name")
    return render(request, "listsapp/listpage.html", {
        "list": list_obj,
        "products": products_in_list,
        "all_products": all_products,
    })

@login_required
def userpage(request):
    if request.method == "POST":
        listname = request.POST.get("listname")
        if listname:
            new_list = List.objects.create(name=listname, user=request.user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    "id": new_list.id,
                    "name": new_list.name,
                    "url": reverse('listpage', args=[new_list.id])
                })
            return redirect("userpage")
            
    lists = List.objects.filter(user=request.user).order_by('-id')
    return render(request, "listsapp/userpage.html", {"lists": lists})


@login_required
def update_address(request, supermarket_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        address = data.get("address")
        supermarket = get_object_or_404(User, id=supermarket_id)
        if request.user != supermarket:
            return JsonResponse({"error": "Unauthorized"}, status=403)
        supermarket.address = address
        supermarket.save()
        return JsonResponse({
            "address": supermarket.address
        })

def supermarketpage(request, supermarket_id):
    supermarket = get_object_or_404(User, id=supermarket_id, is_supermarket=True)
    products = Product.objects.exclude(id__in=PriceMkt.objects.filter(supermarket=supermarket).values_list("product_id", flat=True))
    supermarket_products = PriceMkt.objects.filter(supermarket=supermarket)
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "add_address":
            address = request.POST.get("address")
            if address:
                supermarket.address = address
                supermarket.save()
        elif action == "add_product":
            product_id = request.POST.get("product_id")
            price = request.POST.get("price")
            if product_id and price:
                product = Product.objects.get(id=product_id)
                PriceMkt.objects.create(supermarket=supermarket,product=product,price=price)
        return redirect("supermarketpage", supermarket_id=supermarket.id)
    return render(request, "listsapp/supermarketpage.html", {
        "supermarket": supermarket,
        "products": products,
        "supermarket_products": supermarket_products
    })

def productpage(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == "POST":
        list_id = request.POST.get("list_id")
        if list_id:
            lista_obj = get_object_or_404(List, id=list_id, user=request.user)
            if product not in lista_obj.products.all():
                lista_obj.products.add(product)
                
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({
                        "success": True, 
                        "list_name": lista_obj.name,
                        "list_id": lista_obj.id
                    })
                    
        return redirect("productpage", product_id=product_id)
    
    lists = None
    if request.user.is_authenticated and not request.user.is_supermarket:
         lists = List.objects.filter(user=request.user).exclude(products=product)
         
    return render(request, "listsapp/productpage.html", {
        "product": product,
        "lists": lists
    })

def prices(request, list_id):
    list_obj = get_object_or_404(List, id=list_id, user=request.user)
    products = list_obj.products.all()
    supermarkets = User.objects.filter(is_supermarket=True)
    
    price_per_market = []
    total_products = products.count()
    
    for supermarket in supermarkets:
        total_price = 0
        found_products = 0
        for product in products:
            price_obj = PriceMkt.objects.filter(supermarket=supermarket, product=product).first()
            if price_obj:
                total_price += price_obj.price
                found_products += 1
        if found_products > 0:
            price_per_market.append({
                "supermarket": supermarket,
                "total_price": total_price,
                "found_products": found_products,
                "total_products": total_products,
            })
    price_per_market = sorted(price_per_market, key=lambda x: x['total_price'])
    return render(request, "listsapp/prices.html", {
        "price_per_market": price_per_market,
        "list": list_obj 
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