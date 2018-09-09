from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

import datetime
# Create your models here.
class ServiceRequest(models.Model):
    requested = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  blank=True, null=True, related_name='requested',
                                  limit_choices_to={'is_staff': False})
    manager = models.ForeignKey(settings.AUTH_USER_MODEL,
                                blank=True, null=True, related_name='manager',
                                limit_choices_to={'is_staff':True})
    staff = models.ForeignKey(settings.AUTH_USER_MODEL,
                              blank=True, null=True, related_name='staff',
                              limit_choices_to={'is_staff':True})
    subject = models.CharField(max_length=50)
    problem = models.CharField(max_length=255)
    objective = models.CharField(max_length=255)
    deadline = models.DateField(default='12/31/2018')
    STATUS_CHOICES = (
        ('0', 'Open'),
        ('1', 'Assigned'),
        ('2', 'Completed'),
        ('3', 'Terminated'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Open',blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('services_detail', kwargs={'id':self.id})