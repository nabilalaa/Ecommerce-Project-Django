from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import *
import math
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext


def index(request):
    context = {
        "products": Item.objects.all(),
        "cart": CartItem.objects.all(),
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "cart": CartItem.objects.all(),
    }
    return render(request, "about.html", context)


def products(request):
    context = {
        "products": Item.objects.all(),
        "cart": CartItem.objects.all(),
    }

    return render(request, "products.html", context)


def reviews(request):
    context = {
        "cart": CartItem.objects.all(),
    }
    return render(request, "reviews.html", context)


def contact(request):
    context = {
        "cart": CartItem.objects.all(),
    }
    return render(request, "contact.html", context)


def addItem(request, item_id):
    print(item_id)
    if request.user.is_authenticated:
        item = Item.objects.get(id=item_id)

        cart_item, created = CartItem.objects.get_or_create(
            product=item, user=request.user
        )
        cart_item.quantity += 1
        cart_item.save()
        return redirect("view_cart")
    else:
        return redirect("login")
