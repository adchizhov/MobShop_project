from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from .models import 
from django.utils import timezone

# Create your views here.

def index_page(request):
    if request.method == "GET":
        return HttpResponse('Welcome to nothing')

