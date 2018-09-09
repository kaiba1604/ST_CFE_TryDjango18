from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from .views import contact_view, profile_view

def homeview(request):
    return render(request,'home.html')

urlpatterns = [
    url(r'^$', homeview, name='home'),
    url(r'^$', homeview, name='about'),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', contact_view, name='contact'),
    url(r'^accounts/profile/$', profile_view),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^services/', include('services.urls')),
]
