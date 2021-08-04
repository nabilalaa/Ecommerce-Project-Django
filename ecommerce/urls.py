from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="home"),
    path("about", about, name="about"),
    path("products", products, name="products"),
    path("login", login, name="login"),
    path("register", register, name="register"),
    path("checkout", check_out, name="check_out"),
    path("reviews", reviews, name="reviews"),
    path("details/<int:detail_id>/", details, name="details"),
    path("contact", contact, name="contact"),
]