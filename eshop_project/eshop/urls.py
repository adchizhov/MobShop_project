# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

__author__ = 'adchizhov'

app_name = 'eshop' # обозначил имя приложения для шаблонов йоу!
urlpatterns = [
    # eshop/
    url(r'^$', views.index_page, name='index'),
    # eshop/manufacturers/
    url(r'^manufacturers/$', views.show_manufacturers, name='manufacturers'),
    # /eshop/manufacturers/2/
    url(r'^manufacturers/(?P<manufacturer_id>[0-9]+)/$', views.manufacturer_detail, name='manufacturer_detail'),
]
