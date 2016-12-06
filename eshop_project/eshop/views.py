# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
import logging
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import PhoneProductForm, UserForm
from .models import Manufacturer, PhoneProduct, Order

__author__ = 'adchizhov'


logger = logging.getLogger(__name__)

logger.debug("blah blah blah")
logger.warning("It is a warning")
logger.error("All is broken")


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
        return Manufacturer.objects.all()

# via function
# def show_manufacturers(request):
#     all_manufacturers = Manufacturer.objects.all()
#     count_manufacturers = Manufacturer.objects.count()
#     c = {'all_manufacturers': all_manufacturers, 'count_manufacturers': count_manufacturers}
#     return render(request, 'eshop/manufacturers.html', c)


def manufacturer_detail(request, manufacturer_id):
    # проще через get_object_or_404 чтобы было без трай/эксепт!
    # try:
    #     manuf_detail = Manufacturer.objects.get(pk=manufacturer_id)
    # except Manufacturer.DoesNotExist:
    #     raise Http404("Manufacturer does not exist!")
    manuf_detail = get_object_or_404(Manufacturer, pk=manufacturer_id)
    return render(request, 'eshop/manufacturer_detail.html', {'manuf_detail': manuf_detail})


class PhoneModelsView(generic.ListView):
    template_name = 'eshop/phonemodels.html'
    context_object_name = 'all_phonemodels'

    def get_context_data(self, **kwargs):
        context=super(PhoneModelsView,self).get_context_data(**kwargs)
        context['count_phonemodels'] = PhoneProduct.objects.count()
        return context

    def get_queryset(self):
        return PhoneProduct.objects.all()


def phonemodel_detail(request, phonemodel_id):
    phone_modelname = PhoneProduct.objects.get(pk=phonemodel_id)
    model = get_object_or_404(PhoneProduct, pk=phonemodel_id)
    phone_detail = PhoneProductForm(instance=model)
    return render(request, 'eshop/phonemodel_detail.html',
                  {'phone_detail': phone_detail, 'phone_modelname': phone_modelname})


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


class UserFormView(View):
    form_class = UserForm
    template_name = 'eshop/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('eshop:index') # TODO

        return render(request, self.template_name, {'form': form})