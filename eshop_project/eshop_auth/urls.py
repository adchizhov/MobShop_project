# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib.auth.views import login, logout_then_login
from django.views.generic import CreateView
from .forms import CustomCreationForm
# from .views import register


__author__ = 'adchizhov'


app_name = 'eshop_auth'
urlpatterns = [
    url(r'login/', login,
        {'template_name': 'eshop_auth/login.html'},
        name='login'),
    url(r'logout/', logout_then_login, name='logout'),
    url(r'register/', CreateView.as_view(
        template_name='eshop_auth/register.html',
        form_class=CustomCreationForm,
        success_url='/eshop'
    ), name='register'),
]
