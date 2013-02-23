from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.atados.forms import AuthenticationForm
from atados.nonprofit.views import (NonprofitPictureUpdateView,
                                       NonprofitDetailsUpdateView)
from registration.views import register, activate

urlpatterns = patterns(
    '',

    url(_(r'^nonprofit/sign-up$'), register,
        {'backend': 'atados.nonprofit.backends.RegistrationBackend',
         'template_name': 'atados/nonprofit/sign-up.html'},
        name='sign-up'),

    url(_(r'^nonprofit/sign-up-confirmartion/(?P<activation_key>\w+)$'), activate,
        {'backend': 'atados.nonprofit.backends.RegistrationBackend',
         'template_name': 'atados/nonprofit/sign-up-activation.html'},
        name='sign-up-confirmation'),

    url(_(r'^nonprofit/sign-up-activation-complete$'), direct_to_template, {'template': 'atados/nonprofit/sign-up-activation-complete.html'},
        name='sign-up-activation-complete'),

    url(_(r'^nonprofit/sign-up-complete$'), direct_to_template, {'template': 'atados/nonprofit/sign-up-complete.html'},
        name='sign-up-complete'),

    url(_(r'^(?P<nonprofit>[-\w]+)/edit-nonprofit-picture$'), NonprofitPictureUpdateView.as_view(),
        name='edit-nonprofit-picture'),

    url(_(r'^(?P<nonprofit>[-\w]+)/edit-nonprofit-details$'), NonprofitDetailsUpdateView.as_view(),
        name='edit-nonprofit-details'),
)
