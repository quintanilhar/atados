# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from bootstrap_toolkit.widgets import BootstrapTextInput
from atados.project.models import Project

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
