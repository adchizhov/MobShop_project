import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.encoding import python_2_unicode_compatible # поддержим python 2


@python_2_unicode_compatible
class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50)

    def __str__(self):
        return ('Manufacturer: {}'.format(self.manufacturer_name))

@python_2_unicode_compatible
class PhoneVersion(models.Model):
    gb_16 = ('16 gb', '16 gb version')
    gb_32 = ('32 gb', '32 gb version')
    gb_64 = ('64 gb', '64 gb version')
    gb_128 = ('128 gb', '128 gb version')
    __all = (gb_16, gb_32, gb_64, gb_128)
    version = models.CharField(max_length=5, choices=__all)

    def __str__(self):
        return self.version

@python_2_unicode_compatible
class PhoneProduct(models.Model):
    sku = models.CharField(max_length=15)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    phone_model = models.CharField(max_length=30)
    version = models.ForeignKey('PhoneVersion')
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    stock = models.PositiveSmallIntegerField(default=1)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return ('Product: {}, description: {}, price {}'.format(self.name, self.description, self.price))

@python_2_unicode_compatible
class Address(models.Model):
    full = models.CharField(max_length=150)

    def __str__(self):
        return self.full

@python_2_unicode_compatible
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = PhoneNumberField(default='', unique=True)
    address = models.ForeignKey('Address')
    
    def __str__(self):
        return ('Customer: {} {}'.format(self.first_name, self.last_name))


@python_2_unicode_compatible
class Order(models.Model):
    # стойкое ощущение что здесь многого не хватает
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('PhoneProduct', on_delete=models.CASCADE)
    ordered_datetime = models.DateTimeField()
    comment = models.CharField(max_length=140, blank=True)

    def __str__(self):
        return ('Customer: {} ordered {} at {} with comment {}'.format(
            self.customer, self.product, self.ordered_datetime, self.comment
            ))


