from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

class Product(Page):
    productAt = models.URLField()
    sku = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('sku'), 
        FieldPanel('productAt'), 
        FieldPanel('name'), 
        FieldPanel('image'), 
        FieldPanel('price'), 
        FieldPanel('category'), 
        FieldPanel('description')
]
