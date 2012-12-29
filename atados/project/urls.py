from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.views.generic.edit import CreateView, UpdateView
from django.utils.translation import ugettext_lazy as _
from atados.project.views import CreateProjectView


urlpatterns = patterns(
    '',

    url(_(r'^new$'), CreateProjectView.as_view(), name='new'),
)
