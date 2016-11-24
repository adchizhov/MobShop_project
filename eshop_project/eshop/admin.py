# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import *
# Register your models here.

class CustomManufacturer(admin.ModelAdmin):
    list_display = ('manufacturer_name',)
    search_fields = ('manufacturer_name',)


class CustomPhoneProduct(admin.ModelAdmin):
    list_display = ('manufacturer',
                    'phone_model',
                    'price',
                    'stock',
                    'in_stock',
                    )
    list_per_page = 50
    list_editable = ('price',
                     'stock',
                     )
    search_fields = ('manufacturer',
                     'phone_model',
                     )
    list_filter = ('manufacturer',
                   'phone_model',
                   'price',
                   'stock',
                   'in_stock',
                   )


class CustomCustomer(admin.ModelAdmin):
    list_display = ('first_name',
                    'last_name',
                    'phone_number',
                    'email',
                    'address',
                    )
    search_fields = ('phone_number',
                     'email',
                     'address',
                     )
    list_per_page = 100


class CustomOrder(admin.ModelAdmin):
    list_display = ('order_number',
                    'customer',
                    'product',)
    list_per_page = 100
    date_hierarchy = 'ordered_datetime'


admin.site.register(Manufacturer, CustomManufacturer)
admin.site.register(PhoneProduct, CustomPhoneProduct)
admin.site.register(Customer, CustomCustomer)
admin.site.register(Order, CustomOrder)
