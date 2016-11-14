import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible # support python 2


@python_2_unicode_compatible
class Product(models.Model):
    sku = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    description = models.CharField(max_length=255)

    def __str__(self):
        return ('Product: {}, description: {}, price {}'.format(self.name, self.description, self.price))


@python_2_unicode_compatible
class Manufacturer(models.Model):
    product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    manufacturer_name = models.CharField(max_length=50)

    def __str__(self):
        return ('Manufacturer: {}'.format(self.manufacturer_name))


@python_2_unicode_compatible
class Order(models.Model):
	pass


@python_2_unicode_compatible
class Customer(models.Model):
	pass