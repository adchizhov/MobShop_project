# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import moneyed
from djmoney.models.fields import MoneyField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.encoding import python_2_unicode_compatible  # поддержим python 2


@python_2_unicode_compatible
class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50, unique=True, blank=True, help_text='Пример: Meizu')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return 'Производитель: {}'.format(self.manufacturer_name)


@python_2_unicode_compatible
class PhoneProduct(models.Model):
    sku = models.CharField(max_length=15, help_text='Пример: 107654')
    manufacturer = models.ForeignKey('Manufacturer')
    phone_model = models.CharField(max_length=30, help_text='Пример: Meizu U20')
    chipset = models.CharField(max_length=60, help_text='Пример: MediaTek Helio P10')
    phone_RAM_memory = models.CharField(max_length=40, help_text='Пример: 2/3 ГБ ОЗУ')
    phone_memory = models.CharField(max_length=40, help_text='Пример: 16/32 ГБ встроенная память')
    size_screen = models.CharField(max_length=40, help_text='Пример: 5.5 дюйма FullHD IPS')
    camera = models.CharField(max_length=40, help_text='Пример: 13/5 МП')
    battery = models.CharField(max_length=30, help_text='Пример: 3260 мАч')
    os_version = models.CharField(max_length=50, help_text='Пример: Google Android 6.0, Flyme 5.2.4.0G')
    weight = models.CharField(max_length=20, help_text='Пример: 158 грамм')
    size = models.CharField(max_length=40, help_text='Пример: 153x75x8.2 мм')
    description = models.CharField(max_length=3000, help_text='Пример: Опиши меня красиво')
    price = MoneyField(max_digits=100, decimal_places=2, default_currency='RUB')
    stock = models.PositiveSmallIntegerField(default=10)
    in_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Модель телефона'
        verbose_name_plural = 'Модели телефонов'

    def __str__(self):
        return self.phone_model


@python_2_unicode_compatible
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = PhoneNumberField(default='', help_text='+79036796573')
    address = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return ('Клиент: {} {}'.format(self.first_name, self.last_name))


@python_2_unicode_compatible
class Order(models.Model):
    # стойкое ощущение что здесь многого не хватает
    order_number = models.CharField(max_length=8, default='00000001') # TODO
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    product = models.ForeignKey('PhoneProduct')
    ordered_datetime = models.DateTimeField()
    comment = models.CharField(max_length=140, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return ('Клиент: {} заказал {} от {} с комментарием {}'.format(
            self.customer, self.product, self.ordered_datetime, self.comment
        ))
