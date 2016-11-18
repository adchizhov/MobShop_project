from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Manufacturer,
	PhoneVersion,
	PhoneProduct,
	Address,
	Customer,
	Order,
	)