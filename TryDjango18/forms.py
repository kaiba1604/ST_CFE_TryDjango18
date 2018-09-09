from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=120, required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=255)