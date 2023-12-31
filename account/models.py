from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    image=models.ImageField(upload_to='product_image')
    description=models.CharField(max_length=500)
    options=(
        ('Mobile phone','Mobile phone'),
        ('Earphone','Earphone'),
        ('laptop','laptop'),
        ('Tablet','Tablet'),
        ('Smart watch','Smart watch'),
        ('BT Speaker','BT Speaker')    
    )
    category=models.CharField(max_length=200,choices=options,default='Mobile phone')

class Cart(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='cart')
    # class Meta:
    #     unique_together=('user','product')

    @property
    def totalamnt(self):
        return self.product.price*self.quantity

class Order(models.Model):
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE,related_name='cartorder')
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500,null=True)
    phone=models.IntegerField(null=True)
    options=(
        ('Order Placed','Order Placed'),
        ('Shipped','Shipped'),
        ('Out For Delivery','Out For Delivery'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    status=models.CharField(max_length=100,choices=options)