from email.mime import image
from operator import mod
from unicodedata import name
from django.db import models
from numpy import product
from traitlets import default

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=60)
    catogory=models.CharField(max_length=50, default="")
    sub_catogory=models.CharField(max_length=300,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=30,default="")
    phone=models.CharField(max_length=20,default="")
    desc=models.CharField(max_length=3000,default="")
    

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=6000)
    amount=models.IntegerField(default=0)
    name=models.CharField(max_length=980)
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=6)
    phone=models.CharField(max_length=10, default="")


class OrdersUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=9000)
    timestamp=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.update_desc[0:7]+"..."

    
    

