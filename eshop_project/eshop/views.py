# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
# from .models import 
from django.utils import timezone
import logging
from .forms import *


logger = logging.getLogger(__name__)

logger.debug("blah blah blah")
logger.warning("It is a warning")
logger.error("All is broken")





def index_page(request):
    try:
        if request.method == "GET":
            c = {'ManufacturerForm': ManufacturerForm} # что-то херня какая-то надо подумать
            return render(request, 'eshop/index.html', c)
    except ValueError:
        logger.exception("I know it could happen")