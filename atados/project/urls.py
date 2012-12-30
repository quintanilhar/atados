from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.project.views import ProjectCreateView, ProjectView

urlpatterns = patterns(
    '',

    url(_(r'^project$'), direct_to_template, {'template': 'atados/project/index.html'}, name='index'),
    url(_(r'^(?P<organisation>[-\w]+)/add-new-project$'), ProjectCreateView.as_view(), name='new'),
    url(_(r'^(?P<organisation>[-\w]+)/(?P<project>[-\w]+)$'), ProjectView.as_view(), name='view'),
)
