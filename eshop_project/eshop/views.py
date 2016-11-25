# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse, HttpResponseRedirect, Http404
# from django.utils import timezone
# from django.views import generic
from django.shortcuts import render, get_object_or_404
import logging
from .forms import ManufacturerForm, PhoneProductForm, CustomerForm, OrderForm
from .models import Manufacturer, PhoneProduct, Customer, Order


logger = logging.getLogger(__name__)

logger.debug("blah blah blah")
logger.warning("It is a warning")
logger.error("All is broken")


def index_page(request):
    if request.method == "GET":
        c = {'ManufacturerForm': ManufacturerForm}  # TODO что-то бредни надо подумать
        return render(request, 'eshop/index.html', c)


def show_manufacturers(request):
    if request.method == "GET":
        manufacturers = Manufacturer.objects.all()
        c = {'manufacturers': manufacturers}
        return render(request, 'eshop/manufacturers.html', c)
    else:
        logger.exception("NO POST METHOD!")
