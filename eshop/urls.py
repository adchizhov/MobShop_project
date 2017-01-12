# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

__author__ = 'adchizhov'

app_name = 'eshop'
urlpatterns = [
    # eshop/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # eshop/where
    url(r'^where/$', views.where, name='where'),
    # eshop/onmap
    url(r'^onmap/$', views.OnMap.as_view(), name='onmap'),
    # eshop/manufacturers/
    url(r'^manufacturers/$', views.ManufacturersView.as_view(), name='manufacturers'),
    # eshop/register
    url(r'^register/$', views.register_user, name='register'),
    # eshop/logout
    url(r'^logout/$', views.logout_user, name='logout'),
    # eshop/login
    url(r'^login/$', views.login_user, name='login'),
    # /eshop/manufacturers/2/
    url(r'^manufacturers/(?P<manufacturer_n>[a-zA-Z0-9]+)/$', views.manufacturer_models, name='manufacturer_detail'),
    # /eshop/phonemodels/
    url(r'^phonemodels/$', views.PhoneModelsView.as_view(), name='phonemodels'),
    # /eshop/phonemodels/1
    url(r'^phonemodels/(?P<phone_n>[a-zA-Z0-9 ]+)/$', views.phonemodel_detail, name='phonemodel_detail'),
    # /eshop/make_order/
    url(r'^makeorder/$', views.make_order, name='make_order'),
    # /eshop/order_created
    url(r'^order_created/$', views.OrderCreatedView.as_view(), name='order_created'),
    # /eshop/search
    url(r'^search/$', views.search_function, name='search'),
]
