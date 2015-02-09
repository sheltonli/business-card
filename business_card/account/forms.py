from django import forms
from django.contrib.auth import authenticate
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput
from django.utils.translation import ugettext_lazy as _


class AccountLoginForm(forms.Form):

    email = EmailField(widget=EmailInput(attrs={
        'required': 'required',
        'placeholder': _('Email'),
        'class': 'form-control',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': 'required',
        'placeholder': _('Password'),
        'class': 'form-control',
    }))

    error_messages = {
        'invalid_login': _('Please ensure you entered the correct email and password. Note that the password field is case-sensitive.'),
        'inactive': _('A staff account is required to enter the Flyer Editor program.'),
    }

    def __init__(self, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)
        self.user_cache = None
        self.label_suffix = ''

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(self.error_messages['invalid_login'])
            elif self.user_cache.is_staff is False:
                raise forms.ValidationError(self.error_messages['inactive'])

        return self.cleaned_data

    def get_user(self):
        return self.user_cache
