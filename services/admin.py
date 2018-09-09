from django.contrib import admin
from .models import ServiceRequest
# Register your models here.


class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ['subject','status','requested','manager','staff']
    list_filter = ['status','requested']


admin.site.register(ServiceRequest,ServiceRequestAdmin)

