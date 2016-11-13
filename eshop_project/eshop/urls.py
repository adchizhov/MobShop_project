from django.conf.urls import url

from .views import *

app_name = 'eshop'
urlpatterns = [
    url(r'^$', index_page, name='index'),
]
