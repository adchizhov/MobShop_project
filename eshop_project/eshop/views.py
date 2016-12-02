# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.forms import model_to_dict
from django.http import Http404
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
    return render(request, 'eshop/index.html')


def show_manufacturers(request):
    all_manufacturers = Manufacturer.objects.all()
    count_manufacturers = Manufacturer.objects.count()
    c = {'all_manufacturers': all_manufacturers, 'count_manufacturers': count_manufacturers}
    return render(request, 'eshop/manufacturers.html', c)


def manufacturer_detail(request, manufacturer_id):
    # проще через get_object_or_404 что было без трай/эксепт!
    # try:
    #     manuf_detail = Manufacturer.objects.get(pk=manufacturer_id)
    # except Manufacturer.DoesNotExist:
    #     raise Http404("Manufacturer does not exist!")
    manuf_detail = get_object_or_404(Manufacturer, pk=manufacturer_id)
    return render(request, 'eshop/manufacturer_detail.html', {'manuf_detail': manuf_detail})


def show_phonemodels(request):
    all_phonemodels = PhoneProduct.objects.all()
    count_phonemodels = PhoneProduct.objects.count()
    c = {'all_phonemodels': all_phonemodels, 'count_phonemodels': count_phonemodels}
    return render(request, 'eshop/phonemodels.html', c)


def phonemodel_detail(request, phonemodel_id):
    try:
        phone_modelname = PhoneProduct.objects.get(pk=phonemodel_id)
        phone_detail = PhoneProductForm(data=model_to_dict(PhoneProduct.objects.get(pk=phonemodel_id)))
        # phone_detail = PhoneProduct.objects.filter(id=phonemodel_id).values()
    except PhoneProduct.DoesNotExist:
        raise Http404("Phone does not exist!")
    return render(request, 'eshop/phonemodel_detail.html',
                  {'phone_detail': phone_detail, 'phone_modelname': phone_modelname})