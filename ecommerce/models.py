from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30,null=True)
    description = models.TextField(max_length=50,null=True)
    image = models.ImageField()
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Register(models.Model):
    fullname = models.CharField(max_length=20,null=True)
    username = models.CharField(max_length=50,null=True)
    number = models.CharField(max_length=50,null=True)
    email = models.EmailField(max_length=50,null=True)
    password = models.TextField(max_length=50,null=True)
    rePassword = models.TextField(max_length=50,null=True)
    city = models.CharField(max_length=50,null=True)
    address = models.TextField(max_length=50,null=True)

    def __str__(self):
        return self.fullname


class Login(models.Model):
    name = models.CharField(max_length=20,null=True)
    password = models.TextField(max_length=50,null=True)

    def __str__(self):
        return self.name

class CheckOut(models.Model):
    name = models.CharField(max_length=50,null=True)
    image = models.ImageField(null=True)
    amount = models.IntegerField(null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

class Total(models.Model):
    total = models.FloatField(null=True)
    t = models.FloatField(null=True)

    def __float__(self):
        return self.t

