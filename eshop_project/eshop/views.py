# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.utils import timezone
# from django.views import generic
from django.shortcuts import render, get_object_or_404
import logging
from .forms import ManufacturerForm, PhoneProductForm, CustomerForm, OrderForm
from .models import Manufacturer, PhoneProduct, Customer, Order

__author__ = 'adchizhov'


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
        all_manufacturers = Manufacturer.objects.all()
        count_manufacturers = Manufacturer.objects.count()
        c = {'all_manufacturers': all_manufacturers, 'count_manufacturers': count_manufacturers}
        return render(request, 'eshop/manufacturers.html', c)
    else:
        logger.exception("NO POST METHOD!")


def manufacturer_detail(request, manufacturer_id):
    # проще через get_object_or_404 что было без трай/эксепт!
    # try:
    #     manuf_detail = Manufacturer.objects.get(pk=manufacturer_id)
    # except Manufacturer.DoesNotExist:
    #     raise Http404("Manufacturer does not exist!")
    manuf_detail = get_object_or_404(Manufacturer, pk=manufacturer_id)
    return render(request, 'eshop/manufacturer_detail.html', {'manuf_detail': manuf_detail})
