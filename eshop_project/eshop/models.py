import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible # поддержим python 2


@python_2_unicode_compatible
class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50)

    def __str__(self):
        return ('Manufacturer: {}'.format(self.manufacturer_name))


@python_2_unicode_compatible
class Product(models.Model):
    sku = models.CharField(max_length=15)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.CharField(max_length=250)
    stock = models.PositiveSmallIntegerField(default=1)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return ('Product: {}, description: {}, price {}'.format(self.name, self.description, self.price))


@python_2_unicode_compatible
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    adress = models.CharField(max_length=60)
    
    def __str__(self):
        return ('Customer: {} {}'.format(self.first_name, self.last_name))


@python_2_unicode_compatible
class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    ordered_datetime = models.DateTimeField()
    comment = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return ('Customer: {} ordered {} at {} with comment {}'.format(
        	self.customer, self.product, self.ordered_datetime, self.comment
        	))


