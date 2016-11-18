from django import forms
from django.core.exceptions import ValidationError
from .models import *

class ManufacturerForm(forms.ModelForm):
	class Meta:
		model = Manufacturer
		fields = '__all__'


class PhoneVersionForm(forms.ModelForm):
	class Meta:
		model = PhoneVersion
		fields = '__all__'


class PhoneProductForm(forms.ModelForm):
	class Meta:
		model = PhoneProduct
		fields = '__all__'


class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		fields = '__all__'


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'


class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = '__all__'