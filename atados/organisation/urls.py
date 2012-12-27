from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.atados.forms import AuthenticationForm
from registration.views import register, activate

urlpatterns = patterns(
    '',

    url(_(r'^sign-up$'), register,
        {'backend': 'atados.organisation.backends.RegistrationBackend',
         'template_name': 'atados/organisation/sign-up.html'},
        name='sign-up'),
)
