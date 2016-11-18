from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from .models import 
from django.utils import timezone
from .forms import ManufacturerForm, PhoneVersionForm, PhoneProductForm, AddressForm, CustomerForm, OrderForm

# Create your views here.

def index_page(request):
    if request.method == "GET":
        c = {'PhoneProductForm': PhoneProductForm} # что-то херня какая-то надо подумать
        return render(request, 'eshop/index.html', c)