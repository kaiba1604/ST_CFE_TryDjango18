from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, SignUpForm
# Create your views here.
def signup_view(request):
    print('Debug: Request', request)
    # if request.method=='POST':
    #     print('Debug: print POST data', request.POST)

    form = SignUpForm(request.POST or None)
    context = {
        'form': form,
        'title': 'Signup page'
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        context = {
            'title':'Thank you'
        }

    return render(request, 'newsletter/signup.html',context)

