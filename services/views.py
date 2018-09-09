from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ServiceRequest
from .forms import ServiceForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import get_user
# Create your views here.
#CRUD

def service_list(request):
    if request.user.is_superuser:
        queryset = ServiceRequest.objects.all()
    elif request.user.is_staff:
        queryset = ServiceRequest.objects.filter(Q(manager=request.user)|Q(staff=request.user))
    else:
        queryset = ServiceRequest.objects.filter(requested=request.user)
    context={'queryset': queryset}
    return render(request, 'services/services_list.html', context)

def service_new(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.requested=request.user
        instance.status='0'
        print('Debug:', instance.subject)
        print('Debug:', instance.requested)
        # instance.requested = request.user
        instance.save()
        messages.success(request,'Service Request created.')
        return HttpResponseRedirect(instance.get_absolute_url())

    # form.fields['requested'].initial = request.user.id
    # form.fields['requested'].widget.attrs.update({'disabled': True})
    form.fields['status'].initial = '0'
    form.fields['status'].widget.attrs.update({'disabled': True})

    context = {'form': form}
    return render(request, 'services/services_form.html', context)

def service_detail(request, id=None):
    instance = ServiceRequest.objects.get(id=id)
    form = ServiceForm(instance=instance)

    context = {'form': form, 'disabled':'disabled'}
    return render(request, 'services/services_form.html', context)

def service_edit(request, id=None):
    instance = ServiceRequest.objects.get(id=id)
    form = ServiceForm(instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Service Request created.')
    form.fields['subject'].widget.attrs.update({'disabled':'disabled'})

    context = {'form': form, 'editable':False}
    return render(request, 'services/services_form.html', context)

def service_delete(request):
    queryset = ServiceRequest.objects.all()
    context={'queryset':queryset}
    return render(request, 'services/service_list.html', context)