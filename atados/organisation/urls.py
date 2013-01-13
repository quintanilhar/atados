from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.atados.forms import AuthenticationForm
from atados.organisation.views import OrganisationPictureUpdateView
from registration.views import register, activate

urlpatterns = patterns(
    '',

    url(_(r'^organisation/sign-up$'), register,
        {'backend': 'atados.organisation.backends.RegistrationBackend',
         'template_name': 'atados/organisation/sign-up.html'},
        name='sign-up'),

    url(_(r'^organisation/sign-up-confirmartion/(?P<activation_key>\w+)$'), activate,
        {'backend': 'atados.organisation.backends.RegistrationBackend',
         'template_name': 'atados/organisation/sign-up-activation.html'},
        name='sign-up-confirmation'),

    url(_(r'^organisation/sign-up-activation-complete$'), direct_to_template, {'template': 'atados/organisation/sign-up-activation-complete.html'},
        name='sign-up-activation-complete'),

    url(_(r'^organisation/sign-up-complete$'), direct_to_template, {'template': 'atados/organisation/sign-up-complete.html'},
        name='sign-up-complete'),

    url(_(r'^(?P<organisation>[-\w]+)/edit-organisation-picture$'), OrganisationPictureUpdateView.as_view(),
        name='edit-organisation-picture'),
)
