# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm as ContribAuthenticationForm)
from django.utils.translation import ugettext_lazy as _


class AuthenticationForm(ContribAuthenticationForm):
    username = forms.CharField(label=_('E-mail'), max_length=30)
    rememberme = forms.BooleanField(label=_('Stay signed in'),
                                    initial=True, required=False)
