from django.db import models

# Create your models here.
class Clients(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=150,blank=False)
    tel=models.CharField(max_length=20)
    unable=models.BooleanField(blank=False,default=False)

    def __str__(self) -> str:
        return super().__str__()

class Address(models.Model):
    client=models.ForeignKey(Clients,on_delete=models.CASCADE,blank=False)
    street=models.CharField(max_length=300,blank=False)
    city=models.CharField(max_length=100,blank=False)
    code=models.CharField(max_length=30)
    country=models.CharField(max_length=150,blank=False)

    def __str__(self) -> str:
        return super().__str__()

class Products(models.Model):
    name=models.CharField(max_length=200,blank=False, unique=True)
    imageURL=models.URLField(max_length=500)

    def __str__(self) -> str:
        return super().__str__()

class Products_Details(models.Model):
    BIG = 'BG'
    AVERAGE = 'AV'
    SMALL = 'SM'
    sizes = (
        (BIG, 'BIG'),
        (AVERAGE, 'AVERAGE'),
        (SMALL, 'SMALL')
    )
    product=models.ForeignKey(Products,on_delete=models.CASCADE,blank=False)
    size=models.CharField(choices=sizes,max_length=2,default=AVERAGE)
    weight=models.FloatField(max_length=100,null=True)
    price=models.FloatField(max_length=100,blank=False)
    unable=models.BooleanField(blank=False,default=False)

    class Meta:
        unique_together = (("product", "size"),)

    def __str__(self) -> str:
        return super().__str__()

class Orders(models.Model):
    client=models.ForeignKey(Clients,blank=False,on_delete=models.RESTRICT)
    order_date=models.DateTimeField(blank=False)
    delivery_date=models.DateTimeField()
    billing_address=models.ForeignKey(Address,blank=False,on_delete=models.RESTRICT, related_name='billing')
    shipping_address=models.ForeignKey(Address,blank=False,on_delete=models.RESTRICT,related_name='shipping')

    def __str__(self) -> str:
        return super().__str__()

class Order_Items(models.Model):
    order=models.ForeignKey(Orders,blank=False,on_delete=models.CASCADE)
    product=models.ForeignKey(Products_Details,blank=False,on_delete=models.RESTRICT)
    price=models.FloatField(blank=False)
    quantity=models.IntegerField(blank=False)

    def __str__(self) -> str:
        return super().__str__()