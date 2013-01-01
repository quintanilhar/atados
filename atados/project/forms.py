# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from bootstrap_toolkit.widgets import BootstrapTextInput
from atados.project.models import Project


class ProjectCreateForm(forms.ModelForm):

    name = forms.CharField(max_length=30,
                           widget=forms.TextInput(
                               attrs={'class': 'required'}),
                               label=_("Project name"))

    details = forms.CharField(max_length=30,
                              widget=forms.Textarea(
                              attrs={'class': 'required',
                                     'placeholder': _('Add more info about this proejct')}),
                              label=_("Details"))

    def clean_name(self):
        slug = slugify(self.cleaned_data.get('name'))
        if slug and self.instance.slug != slug and Project.objects.filter(
                slug=slug, organisation=self.organisation).count():
            raise forms.ValidationError(_('This name (or a very similar) is already is use.'))
        return name

    class Meta:
        model = Project
        exclude = ('organisation', 'slug')

class ProjectDonationCreateForm(ProjectCreateForm):
    pass

class ProjectJustOnceCreateForm(ProjectCreateForm):
    pass

class ProjectPeriodicCreateForm(ProjectCreateForm):
    pass
