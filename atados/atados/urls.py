from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _, ugettext
from atados.atados.forms import AuthenticationForm
from registration.views import register, activate

urlpatterns = patterns(
    '',
    url(r'^$', direct_to_template, {'template': 'atados/atados/home.html'},
        name='home'),

    url(_(r'^organisation/sign-up$'), register,
        {'backend': 'atados.atados.backends.RegistrationBackend',
         'template_name': 'atados/atados/organisation/sign-up.html'},
        name='organisation.sign-up'),

    url(_(r'^sign-in$'), 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
         'template_name': 'atados/atados/sign-in.html'}, name='sign-in'),
)
