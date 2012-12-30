from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('atados.atados.urls', namespace='atados')),
    url('', include('atados.organisation.urls', namespace='organisation')),
    url('', include('atados.volunteer.urls', namespace='volunteer')),
    url('', include('atados.project.urls', namespace='project')),
)
