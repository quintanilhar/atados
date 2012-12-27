from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url('', include('atados.atados.urls', namespace='atados')),
    url(_(r'organisation/'), include('atados.organisation.urls', namespace='organisation')),
    url(_(r'volunteer/'), include('atados.volunteer.urls', namespace='volunteer')),
    url(_(r'project/'), include('atados.project.urls', namespace='project')),
)
