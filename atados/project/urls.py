from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic.edit import CreateView, UpdateView
from django.utils.translation import ugettext_lazy as _
from atados.project.models import Project
from atados.project.forms import ProjectCreateForm


urlpatterns = patterns(
    '',

    url(_(r'^new$'), CreateView.as_view(
        model=Project,
        form_class=ProjectCreateForm,
        template_name='atados/project/new.html',
        success_url=''
        ), name='new'),
)
