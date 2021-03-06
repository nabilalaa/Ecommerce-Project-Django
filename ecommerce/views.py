from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import math
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.template import RequestContext


def index(request):
    context = {
        "products": Product.objects.all(),
        "check_out": CheckOut.objects.all(),

    }
    return render(request, "index.html",context)


def about(request):
    context = {
        "check_out": CheckOut.objects.all(),

    }
    return render(request, "about.html",context)


def products(request):
    context = {
        "products": Product.objects.all(),
        "check_out": CheckOut.objects.all(),

    }

    return render(request, "products.html", context)


def reviews(request):
    context = {
        "check_out": CheckOut.objects.all(),

    }
    return render(request, "reviews.html",context)


def contact(request):
    context = {
        "check_out": CheckOut.objects.all(),

    }
    return render(request, "contact.html",context)


def details(request, detail_id):
    name = request.POST.get("name")
    amount = request.POST.get("quantity")
    price = request.POST.get("price")
    image = request.POST.get("image")

    if request.POST and name and price and amount and image:
        print(request.user.is_authenticated)
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            CheckOut.objects.create(
                name=name,
                price=float(amount) * float(price),
                amount=amount,
                image=image,
            )
            Total.objects.create(
                total=(float(amount) * float(price)),
            )
            totalList = Total.objects.all()
            print(totalList)
            listp = []
            for i in range(totalList.count()):
                listp.append(totalList[i].total)

            print(listp)
            t = math.fsum(listp)
            print(t)
            Total.objects.update(
                t=t
            )
            # return redirect("check_out")

    context = {
        "products": Product.objects.filter(id=detail_id),
        "check_out": CheckOut.objects.all(),

    }
    return render(request, "details.html", context)


def check_out(request):
    totalList = Total.objects.all()
    print(totalList)
    listp = []
    for i in range(totalList.count()):
        listp.append(totalList[i].total)

    print(listp)
    t = math.fsum(listp)
    print(t)
    Total.objects.update(
        t=t
    )
    if request.POST and request.POST.get("price"):
        CheckOut.objects.filter(price=request.POST.get("price")).delete()
        Total.objects.filter(total=request.POST.get("price")).delete()
        Total.objects.update(
            t=t - float(request.POST.get("price"))
        )
    context = {
        "check_out": CheckOut.objects.all(),
        "total": Total.objects.first(),
    }
    return render(request, "check-out.html", context)


def log_in(request):
    username = request.POST.get("username")
    password = request.POST.get("pass")
    user = authenticate(username=username, password=password)
    print(user, "ssss")
    if request.method == "POST":
        if user:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "The username is wrong or the password is incorrect")

    return render(request, "login.html")


def register(request):
    fullname = request.POST.get("name")
    username = request.POST.get("user")
    number = request.POST.get("number")
    email = request.POST.get("email")
    password = request.POST.get("password")
    re_password = request.POST.get("re-password")
    city = request.POST.get("city")
    address = request.POST.get("address")
    if request.POST:
        if User.objects.filter(username=username):
            messages.error(request, "username has taken")
        # and len(
        #     password) <= 8
        elif fullname and username and number and email and password == re_password and city and address:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            Register.objects.create(fullname=fullname, city=city, address=address,
                                    username=authenticate(username=username, password=password))
            messages.success(request, "done, register successfully")
            return redirect("login")
        else:
            messages.error(request, "something wrong in form")

    return render(request, "register.html")


def log_out(request):
    logout(request)
    CheckOut.objects.all().delete()
    Total.objects.all().delete()
    return redirect("home")
