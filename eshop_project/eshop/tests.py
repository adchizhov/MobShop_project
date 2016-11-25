# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.test import TestCase
from .models import Manufacturer, PhoneProduct, Customer, Order

__author__ = 'adchizhov'


# Create your tests here.
class TestManufacturer(TestCase):
    def test_manufacturer_creation(self):
        manuf_name = Manufacturer.objects.create(manufacturer_name='Sharp')
        assert manuf_name.pk is not None

    # тесты с использованием фикстур
    fixtures = ['db_v1.json']

    def test_manufacturer_get(self):
        manuf_name = Manufacturer.objects.get(manufacturer_name='Alcatel')
        assert manuf_name is not None

    def test_str_method(self):
        manuf_name = Manufacturer.objects.get(manufacturer_name='Alcatel')
        self.assertEqual(str(manuf_name), 'Производитель: ' + manuf_name.manufacturer_name)


class TestPhoneProduct(TestCase):
    @classmethod
    def setUp(cls):
        cls.manufacturer = Manufacturer.objects.create(manufacturer_name='LG')

    def test_phoneproduct_creation(self):
        ph_prod = PhoneProduct.objects.create(
            sku=107687,
            manufacturer=self.manufacturer,
            phone_model='LG G5',
            chipset='Snapdragon 810',
            phone_RAM_memory='3 ГБ ОЗУ',
            phone_memory='64 ГБ встроенная память',
            size_screen='5.5 дюйма FullHD IPS',
            camera='18/6 МП',
            battery='4500 мАч',
            os_version='Android 6.0',
            weight='170 грамм',
            size='153x75x8.2 мм',
            description='Опиши меня красиво',
            price='40000.00',
            stock=5,
            in_stock=False,
        )
        assert ph_prod.pk is not None

    # тесты с использованием фикстур
    fixtures = ['db_v1.json']

    def test_phoneproduct_get_from_fixtures(self):
        ph_prod_fixt = PhoneProduct.objects.get(phone_model='Meizu U20')
        assert ph_prod_fixt is not None

    def test_str_method(self):
        ph_prod = PhoneProduct.objects.get(sku='107656', chipset='MediaTek Helio P10')
        self.assertEqual(str(ph_prod), ph_prod.phone_model)


class TestCustomer(TestCase):
    def test_customer_creation(self):
        customer = Customer.objects.create(
            first_name='Alice',
            last_name='Demidova',
            email='wonderland@yandex.ru',
            phone_number='+79103478976',
            address='In the galaxy far far away'
        )
        assert customer.pk is not None

    # тесты с использованием фикстур
    fixtures = ['db_v1.json']

    def test_customer_get_from_fixtures(self):
        customer_fixt = Customer.objects.get(first_name='Василий')
        assert customer_fixt is not None


class TestOrder(TestCase):
    @classmethod
    def setUp(cls):
        cls.order_number = '00004567'
        cls.customer = Customer.objects.create(
            first_name='Alice',
            last_name='Demidova',
            email='wonderland@yandex.ru',
            phone_number='+79103478976',
            address='In the galaxy far far away'
        )
        cls.product = PhoneProduct.objects.create(
            sku=107687,
            manufacturer=Manufacturer.objects.create(manufacturer_name='LG'),
            phone_model='LG G5',
            chipset='Snapdragon 810',
            phone_RAM_memory='3 ГБ ОЗУ',
            phone_memory='64 ГБ встроенная память',
            size_screen='5.5 дюйма FullHD IPS',
            camera='18/6 МП',
            battery='4500 мАч',
            os_version='Andoroid 6.0',
            weight='170 грамм',
            size='153x75x8.2 мм',
            description='Опиши меня красиво',
            price='40000.00',
            stock=5,
            in_stock=False,
        )
        cls.ordered_datetime = "2016-11-24T08:25:06Z"
        cls.comment = 'Monty Python'

    def test_order_creation(self):
        order = Order.objects.create(
            order_number=self.order_number,
            customer=self.customer,
            product=self.product,
            ordered_datetime=self.ordered_datetime,
            comment=self.comment)
        assert order.pk is not None

    # тесты с использованием фикстур
    fixtures = ['db_v1.json']

    def test_order_get(self):
        order_fixt = Order.objects.get(product__phone_model__contains='DTEK')
        assert order_fixt is not None
