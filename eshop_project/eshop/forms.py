# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms
from .models import Manufacturer, PhoneProduct, Customer, Order

__author__ = 'adchizhov'


class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'


class PhoneProductForm(forms.ModelForm):
    class Meta:
        model = PhoneProduct
        fields = [
            'sku',
            'manufacturer',
            'phone_model',
            'os_version',
            'chipset',
            'phone_RAM_memory',
            'phone_memory',
            'camera',
            'size_screen',
            'weight',
            'size',
            'description',
            'price'
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
