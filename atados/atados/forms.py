# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import AuthenticationForm as ContribAuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bootstrap_toolkit.widgets import BootstrapTextInput
from registration.forms import RegistrationForm as DefaultRegistrationForm

class RegistrationForm(DefaultRegistrationForm):

    name = forms.CharField(max_length=30,
            widget=forms.TextInput(attrs={'class': 'required', 'tabindex': 1}),
                           label=_("Organization name"))

    username = forms.RegexField(regex=r'^[\w.@+-]+$',
                                max_length=30,
                                widget=BootstrapTextInput(prepend='http://www.atados.com.br/', attrs={'class': 'required', 'tabindex': 2}),
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})

    email = forms.EmailField(widget=forms.TextInput(attrs=dict({'class': 'required', 'tabindex': 3, 'placeholder': _("example@example.com")},
                                                               maxlength=75)),
                                                               label=_("Your e-mail"))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required', 'tabindex': 4}, render_value=False),
                                                           label=_("Create a password"))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'required', 'tabindex': 5}, render_value=False),
                                                           label=_("Confirm your password"))

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields.keyOrder = [
                'name',
                'username',
                'email',
                'password1',
                'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError(_('This e-mail is already is use.'))
        return email

class AuthenticationForm(ContribAuthenticationForm):
    username = forms.CharField(label=_('E-mail'), max_length=30)
    rememberme = forms.BooleanField(label=_('Remember me'), initial=True) 
