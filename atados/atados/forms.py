# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm as ContribAuthenticationForm)
from django.utils.translation import ugettext_lazy as _
from haystack.forms import SearchForm as HaystackSearchForm, model_choices
from atados.nonprofit.models import Nonprofit
from atados.project.models import ProjectDonation, ProjectWork
from atados.volunteer.models import Volunteer


SEARCH_TYPES = (
        ('Nonprofit', 'Nonprofit'),
        ('Project', 'Project'),
        ('Volunteer', 'Volunteer'),)

class SearchForm(HaystackSearchForm):
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['types'] = forms.MultipleChoiceField(choices=SEARCH_TYPES, required=False, label=_('Search In'), widget=forms.CheckboxSelectMultiple)

    def get_models(self):
        """Return an alphabetical list of model classes in the index."""
        search_models = []

        if self.is_valid():
            if 'Nonprofit' in self.cleaned_data['types']:
                search_models.append(Nonprofit)
            if 'Volunteer' in self.cleaned_data['types']:
                search_models.append(Volunteer)
            if 'Project' in self.cleaned_data['types'] or not search_models:
                search_models.append(ProjectDonation)
                search_models.append(ProjectWork)

        return search_models

    def search(self):
        sqs = super(SearchForm, self).search()
        return sqs.models(*self.get_models())

class AuthenticationForm(ContribAuthenticationForm):
    username = forms.CharField(label=_('E-mail'), max_length=30)
    rememberme = forms.BooleanField(label=_('Stay signed in'),
                                    initial=True, required=False)
