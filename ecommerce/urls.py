from django.urls import path
from .views import *


urlpatterns = [
    path("",index,name="home"),
    path("about", about, name="about"),
    path("products", products, name="products"),
    # path("login", log_in, name="login"),
    # path("logout", log_out, name="logout"),
    # path("register", register, name="register"),
    # path("checkout", check_out, name="check_out"),
    path("reviews", reviews, name="reviews"),
    path("additem/<int:item_id>", addItem, name="addItem"),
    path("contact", contact, name="contact"),
]