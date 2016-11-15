# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 08:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('adress', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_datetime', models.DateTimeField()),
                ('comment', models.CharField(blank=True, max_length=140)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('description', models.CharField(max_length=250)),
                ('stock', models.PositiveSmallIntegerField(default=1)),
                ('in_stock', models.BooleanField(default=True)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.Manufacturer')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.Product'),
        ),
    ]
