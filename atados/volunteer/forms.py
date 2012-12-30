# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bootstrap_toolkit.widgets import BootstrapTextInput
from registration.forms import RegistrationForm as DefaultRegistrationForm


class RegistrationForm(DefaultRegistrationForm):

    first_name = forms.CharField(max_length=30,
                           widget=forms.TextInput(
                               attrs={'class': 'required',
                                      'tabindex': 1,
                                      'placeholder': _("Your first name")}),
                           label=_("Name"))

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs=dict({'class': 'required',
                        'tabindex': 3,
                        'placeholder': _("example@example.com")},
                       maxlength=75)),
        label=_("Your e-mail"))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'required', 'tabindex': 4}, render_value=False),
        label=_("Create a password"))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'required', 'tabindex': 5}, render_value=False),
        label=_("Confirm your password"))

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields.keyOrder = ['first_name',
                                'email',
                                'password1',
                                'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(
                username=username).count():
            raise forms.ValidationError(_('This e-mail is already is use.'))
        return email

