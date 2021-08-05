from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import math


def index(request):
    context = {
        "products": Product.objects.all(),
        "login": Login.objects.all(),
        "title": "home"
    }
    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()
        return redirect("home")
    return render(request, "index.html", context)


def about(request):
    context = {
        "products": Product.objects.all(),
        "login": Login.objects.all(),
        "title": "about"

    }
    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()
        return redirect("home")

    return render(request, "about.html", context)


def products(request):
    context = {
        "products": Product.objects.all(),
        "login": Login.objects.all(),
        "title":"products"
    }

    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()
        return redirect("home")

    return render(request, "products.html", context)


def reviews(request):
    context = {
        "products": Product.objects.all(),
        "login": Login.objects.all(),
        "title": "reviews"

    }
    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()

        return redirect("home")

    return render(request, "reviews.html", context)


def contact(request):
    context = {
        "products": Product.objects.all(),
        "login": Login.objects.all(),
        "title": "contact"

    }
    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()

        return redirect("home")

    return render(request, "contact.html", context)


def details(request, detail_id):
    name = request.GET.get("name")
    amount = request.GET.get("quantity")
    price = request.GET.get("price")
    image = request.GET.get("image")

    if request.GET and name and price and amount and image:
        if not Login.objects.all():
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
            return redirect("check_out")

    context = {
        "products": Product.objects.filter(id=detail_id),
        "login": Login.objects.all(),
        "title": "details"

    }
    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()
        return redirect("home")
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
    if request.GET and request.GET.get("price"):
        CheckOut.objects.filter(price=request.GET.get("price")).delete()
        Total.objects.filter(total=request.GET.get("price")).delete()
        Total.objects.update(
            t=t-float(request.GET.get("price"))
        )

    if request.POST:
        Login.objects.all().delete()
        CheckOut.objects.all().delete()

        return redirect("home")
    context = {
        "check_out": CheckOut.objects.all(),
        "login": Login.objects.all(),
        "total": Total.objects.first(),
        "title": "check_out"

    }
    return render(request, "check-out.html", context)


def login(request):
    username = request.POST.get("username")
    password = request.POST.get("pass")
    if request.POST:
        if Register.objects.filter(username=username, password=password):
            Login.objects.create(name=username, password=password)
            return redirect("home")

        else:
            messages.error(request, "The username is wrong or the password is incorrect")

    print(username, password)
    return render(request, "login.html",context={"title": "login"})


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
        if fullname and username and number and email and password == re_password and city and address:
            Register.objects.create(
                fullname=fullname,
                username=username,
                number=number,
                email=email,
                password=password,
                rePassword=re_password,
                city=city,
                address=address
            )
            messages.success(request, "done, register successfully")

        else:
            messages.error(request, "something wrong in form")

    return render(request, "register.html",context={"title": "register"})
