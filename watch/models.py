from django.db import models
#   img: string;
#   name: string;
#   description: string;
#   oldPrice: number;
#   newPrice: number;
# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=250)
    number = models.CharField(max_length=250)
    comment = models.TextField(blank=True)

    name = models.CharField(max_length=250,blank=True,default="watch_name")
    description = models.TextField(blank=True)
    oldPrice = models.DecimalField(max_digits=10,decimal_places=2,default=1)
    newPrice = models.DecimalField(max_digits=10,decimal_places=2,default=1)
    

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    name = models.CharField(max_length=250,blank=True,default="watch_name")
    description = models.TextField(blank=True)
    oldPrice = models.DecimalField(max_digits=10,decimal_places=2,default=1)
    newPrice = models.DecimalField(max_digits=10,decimal_places=2,default=1)
    img = models.ImageField(upload_to="pics") #(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)