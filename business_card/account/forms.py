from django import forms
from django.contrib.auth import authenticate
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput
from django.utils.translation import ugettext_lazy as _
from business_card.account.models import User
from business_card.core.utils import get_object_or_none


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


class AccountRegisterForm(forms.ModelForm):

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

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'required': 'required',
        'placeholder': _('Confirm Password'),
        'class': 'form-control',
    }))

    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('Full Name'),
        'class': 'form-control',
    }))

    address = forms.CharField(
        widget = forms.TextInput(attrs={
            'required': 'required',
            'placeholder': _('Address Line 1'),
            'class': 'form-control',
        }),
        label = 'Address Line 1',
    )

    address_2 = forms.CharField(
        widget = forms.TextInput(attrs={
            'placeholder': _('Address Line 2'),
            'class': 'form-control',
        }),
        label = 'Address Line 2',
    )

    city = forms.CharField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('City'),
        'class': 'form-control',
    }))

    country = forms.CharField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('Country'),
        'class': 'form-control',
    }))

    province_state = forms.CharField(
        widget = forms.TextInput(attrs={
            'required': 'required',
            'placeholder': _('Province/State'),
            'class': 'form-control',
        }),
        label = 'Province/State',
    )

    postal_code = forms.CharField(widget=forms.TextInput(attrs={
        'required': 'required',
        'placeholder': _('Postal Code'),
        'class': 'form-control',
    }))

    phone_number = forms.RegexField(
        widget=forms.TextInput(attrs={
            'required': 'required',
            'placeholder': _('Phone Number'),
            'class': 'form-control',
        }),
        regex = r'^\+?1?\d{9,15}$',
        error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))

    error_messages = {
        'invalid_login': _('Please ensure you entered the correct email and password. Note that the password field is case-sensitive.'),
        'inactive': _('A staff account is required to enter the Flyer Editor program.'),
    }

    def __init__(self, *args, **kwargs):
        super(AccountRegisterForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']
        exclude = ['last_login', 'is_staff', 'is_active', 'created_on', 'updated_on']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        user = get_object_or_none(User, email=email)
        if user:
            raise forms.ValidationError(self.error_messages['duplicate_email'])

        return email

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_('The passwords entered did not match.'))
        return password2

    def save(self, commit=True):
        user = super(AccountRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.password = user.set_password(self.cleaned_data.get('password'))
        user.full_name = self.cleaned_data.get('full_name')
        user.address = self.cleaned_data.get('address')
        user.address2 = self.cleaned_data.get('address2')
        user.city = self.cleaned_data.get('city')
        user.county = self.cleaned_data.get('country')
        user.province_state = self.cleaned_data.get('province_state')
        user.postal_code = self.cleaned_data.get('postal_code')
        user.phone_number = self.cleaned_data.get('phone_number')
        if commit:
            user.save()
        return user