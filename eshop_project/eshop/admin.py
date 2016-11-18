from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Manufacturer)
admin.site.register(PhoneVersion)
admin.site.register(PhoneProduct)
admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Order)
	