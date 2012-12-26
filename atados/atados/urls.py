from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _, ugettext
from registration.views import register, activate

urlpatterns = patterns(
    '',
    url(r'^$', direct_to_template, {'template': 'atados/atados/home.html'},
        name='home'),
)
