# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from bootstrap_toolkit.widgets import BootstrapTextInput
from atados.project.models import Project


class ProjectCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(
                               attrs={'class': 'required'}),
                               label=_("Project name"))

    slug = forms.RegexField(regex=r'^[\w-]+$',
                                max_length=30,
                                label=_("Project address"),
                                error_messages={'invalid':
                                                _("This value may contain "
                                                  "only letters, numbers a"
                                                  "nd \"-\" character.")
                                                })

    details = forms.CharField(max_length=30,
                              widget=forms.Textarea(
                              attrs={'class': 'required',
                                     'placeholder': _('Add more info')}),
                              label=_("Details"))

    def __init__(self, organisation=None, *args, **kwargs):
        super(ProjectCreateForm, self).__init__(*args, **kwargs)
        self.fields['slug'].widget = BootstrapTextInput(
                                    prepend='http://www.atados.com.br/' + organisation.slug + '/',
                                    attrs={'class': 'required'})

    class Meta:
        model = Project
        exclude = ('organisation')
