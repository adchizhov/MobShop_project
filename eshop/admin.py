# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from .models import Manufacturer, PhoneProduct, Order

__author__ = 'adchizhov'


# Register your models here.


class CustomManufacturer(admin.ModelAdmin):
    list_display = ('manufacturer_name', 'manufacturer_info')
    search_fields = ('manufacturer_name',)
    list_editable = ('manufacturer_info',)


class CustomPhoneProduct(admin.ModelAdmin):
    list_display = (
        'id',
        'manufacturer',
        'phone_model',
        'price',
        'stock',
        'in_stock',
    )
    list_per_page = 50
    list_editable = (
        'phone_model',
        'price',
        'stock',
    )
    search_fields = (
        'manufacturer',
        'phone_model',
    )
    list_filter = (
        'manufacturer',
        'phone_model',
        'price',
        'stock',
        'in_stock',
    )


class CustomOrder(admin.ModelAdmin):
    list_display = (
        'product',
        'first_name',
        'last_name',
        'phone_number',
        'address',
        'comment',
    )
    list_per_page = 100
    date_hierarchy = 'ordered_datetime'


admin.site.register(Manufacturer, CustomManufacturer)
admin.site.register(PhoneProduct, CustomPhoneProduct)
# admin.site.register(Customer, CustomCustomer)
admin.site.register(Order, CustomOrder)
