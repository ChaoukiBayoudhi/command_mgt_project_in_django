from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.
class Product(models.Model):
    label = models.CharField(max_length=50,default='')
    price = models.FloatField(default=0.0)
    stock=models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table='product'
    def __str__(self):
        return self.label

class Client(models.Model):
    name=models.CharField(max_length=50,default='')
    birthDate=models.DateField(default= date(2000,1,1)) 
    #birthDate=models.DateField(default=timezone.now)
    #specification of the many to many relationship between Client and Product
    client_products=models.ManyToManyField(Product,through='Command',through_fields=('clt','prod'))
    class Meta:
        db_table='client'
    def __str__(self):
        return self.name

class Command(models.Model):
    prod=models.ForeignKey(Product,on_delete=models.CASCADE)
    clt=models.ForeignKey(Client,on_delete=models.CASCADE)
    date=models.DateField(default=timezone.now)
    quantity=models.PositiveSmallIntegerField(default=0)
    class Meta:
        db_table='command'
    def __str__(self):
        return str(self.id)