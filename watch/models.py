from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250,blank=True,default="watch_name")
    description = models.TextField(blank=True,default="hello",null=True)
    oldPrice = models.DecimalField(max_digits=10,decimal_places=2,default=1)
    newPrice = models.DecimalField(max_digits=10,decimal_places=2,default=1)
    top = models.BooleanField(default=False)
    img = models.ImageField(upload_to="pics",default="hello1") #(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
class Order(models.Model):
    customer_name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    comment = models.TextField(blank=True)
    products = models.ManyToManyField(Product,blank=True,null=True)#, verbose_name=_(""))

class Discount(models.Model):
    time = models.DateTimeField()

