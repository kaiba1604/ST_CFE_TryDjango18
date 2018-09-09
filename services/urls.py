from django.conf.urls import url
from django.shortcuts import render
from django.http import HttpResponse
def service_homeview(request):
    return HttpResponse('<h1> This is Service home page </h1>')

from .views import service_list, service_new, service_detail, service_edit

urlpatterns = [
    url(r'^$', service_list, name='services'),
    url(r'^new$', service_new, name='services_new'),
    url(r'^(?P<id>\d+)$', service_detail, name='services_detail'),
    url(r'^(?P<id>\d+)/edit$', service_edit, name='services_edit'),

]