# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils import timezone
from djmoney.models.fields import MoneyField
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse
# поддержим python 2
from django.utils.encoding import python_2_unicode_compatible


__author__ = 'adchizhov'


@python_2_unicode_compatible
class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=50, unique=True, blank=True, help_text='Пример: Meizu')
    manufacturer_info = models.CharField(max_length=3000)

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return 'Производитель: {}'.format(self.manufacturer_name)


@python_2_unicode_compatible
class PhoneProduct(models.Model):
    sku = models.CharField(
        max_length=15,
        help_text='Пример: 107654',
        verbose_name="Артикул")
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        to_field='manufacturer_name',
        verbose_name="Производитель"
    )
    phone_model = models.CharField(
        max_length=30,
        help_text='Пример: Meizu U20',
        verbose_name='Модель телефона'
    )
    chipset = models.CharField(
        max_length=60,
        help_text='Пример: MediaTek Helio P10',
        verbose_name='Чипсет'
    )
    phone_RAM_memory = models.CharField(
        max_length=40,
        help_text='Пример: 2/3 ГБ ОЗУ',
        verbose_name='Оперативная память'
    )
    phone_memory = models.CharField(
        max_length=40,
        help_text='Пример: 16/32 ГБ встроенная память',
        verbose_name='Постоянная память'
    )
    size_screen = models.CharField(
        max_length=40,
        help_text='Пример: 5.5 дюйма FullHD IPS',
        verbose_name='Размер экрана'
    )
    camera = models.CharField(
        max_length=40,
        help_text='Пример: 13/5 МП',
        verbose_name='Камера'
    )
    battery = models.CharField(
        max_length=30,
        help_text='Пример: 3260 мАч',
        verbose_name='Емкость батареи'
    )
    os_version = models.CharField(
        max_length=50,
        help_text='Пример: Google Android 6.0, Flyme 5.2.4.0G',
        verbose_name='Операционная система'
    )
    weight = models.CharField(
        max_length=20,
        help_text='Пример: 158 грамм',
        verbose_name='Вес'
    )
    size = models.CharField(
        max_length=40,
        help_text='Пример: 153x75x8.2 мм',
        verbose_name='Размер'
    )
    description = models.CharField(
        max_length=3000,
        help_text='Пример: Опиши меня красиво',
        verbose_name='Описание'
    )
    price = MoneyField(
        max_digits=100,
        decimal_places=2, default_currency='RUB',
        verbose_name='Цена'
    )
    stock = models.PositiveSmallIntegerField(
        default=10,
        verbose_name='Осталось'
    )
    in_stock = models.BooleanField(
        default=True,
        verbose_name='Наличие'
    )
    image = models.ImageField()

    class Meta:
        verbose_name = 'Модель телефона'
        verbose_name_plural = 'Модели телефонов'

    def __str__(self):
        return self.phone_model


# @python_2_unicode_compatible
# class Customer(models.Model):
#     first_name = models.CharField(max_length=15)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField()
#     phone_number = PhoneNumberField(default='', help_text='+79036796573')
#     address = models.CharField(max_length=150)
#
#     class Meta:
#         verbose_name = 'Клиент'
#         verbose_name_plural = 'Клиенты'
#
#     def __str__(self):
#         return 'Клиент: {} {}'.format(self.first_name, self.last_name)


@python_2_unicode_compatible
class Order(models.Model):
    first_name = models.CharField(max_length=15, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='E-Mail')
    phone_number = PhoneNumberField(default='', help_text='+79036796573', verbose_name='Номер телефона')
    address = models.CharField(max_length=150, verbose_name='Адрес доставки')
    product = models.ForeignKey('PhoneProduct', verbose_name='Модель телефона')
    ordered_datetime = models.DateTimeField(
        blank=True,
        null=True,
        default=timezone.now,
        verbose_name='Дата и время заказа'
    )
    comment = models.CharField(max_length=140, blank=True, verbose_name='Комментарий к зазазу')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def get_absolute_url(self):
        return reverse('eshop:order_created')

    def __str__(self):
        return 'Клиент: {} заказал {} от {} с комментарием {}'.format(
            self.last_name, self.product, self.ordered_datetime, self.comment
        )
