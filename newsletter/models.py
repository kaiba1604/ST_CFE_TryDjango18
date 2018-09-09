from django.db import models
from django import forms
# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    FirstName = models.CharField(max_length=50, default='First', verbose_name='First Name')
    LastName = models.CharField(max_length=50, default='Last', verbose_name='Last Name')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.email
