from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.project.views import ProjectCreateView

urlpatterns = patterns(
    '',

    url(r'^$', direct_to_template, {'template_name', 'atados/project/index.html'}, name='index'),
    url(_(r'^new$'), ProjectCreateView.as_view(), name='new'),
)
