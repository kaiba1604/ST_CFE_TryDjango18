from django.conf.urls import url
from django.shortcuts import render
from .views import signup_view

def newsletter_homeview(request):
    return render(request,'base.html')

urlpatterns = [
    url(r'^$', signup_view, name='signup'),

]
