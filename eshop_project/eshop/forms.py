# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from .models import PhoneProduct

__author__ = 'adchizhov'


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
            'price',
        ]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['email'].label = 'E-mail'
        self.fields['password'].label = 'Пароль'