# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

__author__ = 'adchizhov'

app_name = 'eshop'  # обозначил имя приложения для шаблонов йоу!
urlpatterns = [
    # eshop/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # eshop/manufacturers/
    url(r'^manufacturers/$', views.ManufacturersView.as_view(), name='manufacturers'),
    # eshop/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # eshop/logout
    url(r'^logout/$', views.logout_user, name='logout'),
    # eshop/login
    url(r'^login/$', views.login_user, name='login'),
    # /eshop/manufacturers/2/
    url(r'^manufacturers/(?P<manufacturer_id>[0-9]+)/$', views.manufacturer_detail, name='manufacturer_detail'),
    # /eshop/phonemodels/
    url(r'^phonemodels/$', views.PhoneModelsView.as_view(), name='phonemodels'),
    # /eshop/phonemodels/1
    url(r'^phonemodels/(?P<phonemodel_id>[0-9]+)/$', views.phonemodel_detail, name='phonemodel_detail'),
    # /eshop/make_order/
    url(r'^makeorder/$', views.OrderCreate.as_view(), name='make_order'),
    # /eshop/order_created
    url(r'^order_created/$', views.OrderCreatedView.as_view(), name='order_created'),
]
