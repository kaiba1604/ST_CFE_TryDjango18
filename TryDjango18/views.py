from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def contact_view(request):
    form = ContactForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_full_name = form.cleaned_data.get('fullname')
        send_mail(subject='Thank you for contacting',
                  message="""
Hi {}, 
Thank you for contacting us. We will get back to you shortly.
                  """.format(form_full_name),
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[form_email],
                  # from_email=settings.EMAIL_HOST_USER,
                  fail_silently=False,  # Should be on
                  )
    return render(request, 'contact.html',context)

def profile_view(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect(reverse('auth_login'))
    # elif request.user.is_superuser():
    #     return HttpResponseRedirect(reverse('services_list'))
    # elif request.user.is_staff():
    #     return render(request, 'registration/profile_staff.html')
    else:
        return HttpResponseRedirect(reverse('services'))
