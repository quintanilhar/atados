# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from bootstrap_toolkit.widgets import BootstrapTextInput
from registration.forms import RegistrationForm as DefaultRegistrationForm
from atados.nonprofit.models import Nonprofit


class RegistrationForm(DefaultRegistrationForm):

    nonprofit_name = forms.CharField(max_length=30,
                           widget=forms.TextInput(
                               attrs={'class': 'required'}),
                           label=_("Nonprofit name"))

    slug = forms.RegexField(regex=r'^[\w-]+$',
                            max_length=30,
                            widget=BootstrapTextInput(
                                prepend='http://www.atados.com.br/',
                                attrs={'class': 'required'}),
                            label=_("Nonprofit address"),
                            error_messages={'invalid':
                                            _("This value may contain "
                                              "only letters, numbers a"
                                              "nd \"-\" character.")
                                            })

    first_name = forms.CharField(max_length=30,
                           widget=forms.TextInput(
                               attrs={'class': 'required'}),
                           label=_("Your name"))


    email = forms.EmailField(
        widget=forms.TextInput(
            attrs=dict({'class': 'required',
                        'placeholder': _("example@example.com")},
                       maxlength=75)),
        label=_("Your e-mail"))

    username = forms.RegexField(regex=r'^[\w-]+$',
                                max_length=30,
                                widget=forms.TextInput(
                                    attrs=dict({'class': 'required'},
                                    maxlength=75)),
                                label=_("Username"),
                                error_messages={'invalid':
                                                _("This value may contain "
                                                  "only letters, numbers a"
                                                  "nd \"-\" character.")
                                                })

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'required' }, render_value=False),
        label=_("Create a password"))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'required'}, render_value=False),
        label=_("Confirm your password"))

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields.keyOrder = ['nonprofit_name',
                                'slug',
                                'first_name',
                                'email',
                                'username',
                                'password1',
                                'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and (
                User.objects.filter(username=username).count() or
                Nonprofit.objects.filter(slug=username).count()):
            raise forms.ValidationError(_('This username is already is use.'))
        return username

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if slug and (
                User.objects.filter(username=slug).count() or
                Nonprofit.objects.filter(slug=slug).count()):
            raise forms.ValidationError(_('This nonprofit address is already is use.'))
        return slug

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(
                username=username).count():
            raise forms.ValidationError(_('This e-mail is already is use.'))
        return email

class NonprofitPictureForm(forms.ModelForm):
    class Meta:
        model = Nonprofit
        fields = ('image',)

class NonprofitDetailsForm(forms.ModelForm):
    class Meta:
        model = Nonprofit
        fields = ('details',)
