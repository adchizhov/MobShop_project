# -*- coding: utf-8 -*-
from django.conf.urls import url
from .views import *

__author__ = 'adchizhov'


app_name = 'eshop'
urlpatterns = [
    url(r'^$', index_page, name='index'),
    url(r'^manufacturers/$', show_manufacturers, name='manufacturers'),
]
