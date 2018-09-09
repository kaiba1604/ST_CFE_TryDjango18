from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email','FirstName','LastName']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not "edu" in email:
            raise forms.ValidationError('Please use a valid .edu email address')
        return email


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=120, required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=255)
