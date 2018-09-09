from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm

# admin.site.register(SignUp) #Standard admin site

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['__str__','email','timestamp','updated']
    form = SignUpForm
    # class Meta:
    #     model = SignUp

admin.site.register(SignUp, SignUpAdmin)