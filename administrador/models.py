from django.db import models

# Create your models here.
class Address(models.Model):
    FULL = 'FL'
    SHIPPING = 'SH'
    BILLING = 'BL'
    address_types = (
        (SHIPPING, 'SHIPPING'),
        (BILLING, 'BILLING'),
        (FULL, 'FULL')
    )
    street=models.CharField(max_length=300,blank=False)
    city=models.CharField(max_length=100,blank=False)
    code=models.CharField(max_length=30)
    country=models.CharField(max_length=150,blank=False)
    type=models.CharField(address_types,max_length=2,default=FULL)

class Clients(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=150,blank=False)
    tel=models.CharField(max_length=20)
    address=models.ForeignKey(Address,on_delete=models.RESTRICT,blank=False)
    imageURL=models.URLField(max_length=500)
    unable=models.BooleanField(blank=False,default=False)

    def __str__(self) -> str:
        return super().__str__()

class Products(models.Model):
    BIG = 'BG'
    AVERAGE = 'AV'
    SMALL = 'SM'
    sizes = (
        (BIG, 'BIG'),
        (AVERAGE, 'AVERAGE'),
        (SMALL, 'SMALL')
    )
    name=models.CharField(max_length=200,blank=False, unique=True)
    size=models.EmailField(sizes,max_length=2,default=AVERAGE)
    weight=models.FloatField(max_length=100)
    price=models.FloatField(max_length=100,blank=False)
    imageURL=models.URLField(max_length=500)
    unable=models.BooleanField(blank=False,default=False)

    def __str__(self) -> str:
        return super().__str__()

class Orders(models.Model):
    client=models.ForeignKey(Clients,blank=False,on_delete=models.RESTRICT)
    order_date=models.DateTimeField(blank=False)
    delivery_date=models.DateTimeField()
    unable=models.BooleanField(blank=False,default=False)

    def __str__(self) -> str:
        return super().__str__()

class Order_Items(models.Model):
    order=models.ForeignKey(Orders,blank=False,on_delete=models.RESTRICT)
    product=models.ForeignKey(Products,blank=False,on_delete=models.RESTRICT)
    quantity=models.IntegerField(max_length=100,blank=False)

    def __str__(self) -> str:
        return super().__str__()