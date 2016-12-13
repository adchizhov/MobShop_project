# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import PhoneProductForm, UserForm
from .models import Manufacturer, PhoneProduct, Order

__author__ = 'adchizhov'

logger = logging.getLogger(__name__)

logger.debug("Low level system information for debugging purposes")
logger.warning("Information describing a minor problem that has occurred.")
logger.error("Information describing a major problem that has occurred.")


class IndexView(generic.TemplateView):
    template_name = 'eshop/index.html'


class OrderCreatedView(generic.TemplateView):
    template_name = "eshop/order_created.html"


class ManufacturersView(generic.ListView):
    template_name = 'eshop/manufacturers.html'
    context_object_name = 'all_manufacturers'

    def get_context_data(self, **kwargs):
        context = super(ManufacturersView, self).get_context_data(**kwargs)
        context['count_manufacturers'] = Manufacturer.objects.count()
        return context

    def get_queryset(self):
        return Manufacturer.objects.all().order_by('manufacturer_name')


# via function
# def show_manufacturers(request):
#     all_manufacturers = Manufacturer.objects.all()
#     count_manufacturers = Manufacturer.objects.count()
#     c = {'all_manufacturers': all_manufacturers, 'count_manufacturers': count_manufacturers}
#     return render(request, 'eshop/manufacturers.html', c)
#


def manufacturer_models(request, manufacturer_id):
    try:
        manufacturer = Manufacturer.objects.get(pk=manufacturer_id)
        manuf_models = manufacturer.phoneproduct_set.all()
    except Manufacturer.DoesNotExist:
        raise Http404("Нет такого производителя!")
    return render(
        request,
        'eshop/manufacturer_models.html',
        {'manuf_models': manuf_models, 'manuf_detail': manufacturer}
    )


class PhoneModelsView(generic.ListView):
    template_name = 'eshop/phonemodels.html'
    context_object_name = 'all_phonemodels'

    def get_context_data(self, **kwargs):
        context = super(PhoneModelsView, self).get_context_data(**kwargs)
        context['count_phonemodels'] = PhoneProduct.objects.count()
        return context

    def get_queryset(self):
        return PhoneProduct.objects.all().order_by('phone_model')


def phonemodel_detail(request, phonemodel_id):
    try:
        phone_model = PhoneProduct.objects.get(pk=phonemodel_id)
        phone_detail = PhoneProductForm(instance=phone_model)
    except PhoneProduct.DoesNotExist:
        raise Http404("Нет такой модели!")
    return render(request, 'eshop/phonemodel_detail.html',
                  {'phone_detail': phone_detail, 'phone_modelname': phone_model})


class OrderCreate(CreateView):
    model = Order
    fields = [
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'address',
        'product',
        'comment',
    ]


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('eshop:index')
    return render(request, 'eshop/registration_form.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('eshop:index')  # TODO!!!
        else:
            return render(request, 'eshop/login.html', {'error_message': 'Неверный логин или пароль'})
    return render(request, 'eshop/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'eshop/index.html', context)


def search_function(request):
    manufacturers = Manufacturer.objects.all()
    phone_models = PhoneProduct.objects.all()
    query = request.GET.get("q")
    if query:
        manufacturers_results = manufacturers.filter(
            Q(manufacturer_name__icontains=query) |
            Q(manufacturer_info__icontains=query)
        ).distinct()
        phone_results = phone_models.filter(
            Q(phone_model__icontains=query)
        ).distinct()
        return render(request, 'eshop/search_page.html', {
            'manufacturers_results': manufacturers_results,
            'phone_results': phone_results,
        })
    else:
        return render(request, 'eshop/search_page.html')

# via class
# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'eshop/registration_form.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#             user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('eshop:index')
#
#         return render(request, self.template_name, {'form': form})
