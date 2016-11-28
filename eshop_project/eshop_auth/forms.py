# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

__author__ = 'adchizhov'


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2')