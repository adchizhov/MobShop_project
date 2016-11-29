# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import CustomUser

__author__ = 'adchizhov'


# Register your models here.

class CustomCustomUser(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomCustomUser)
