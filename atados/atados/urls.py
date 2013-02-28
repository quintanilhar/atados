from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.atados.forms import AuthenticationForm, SearchForm
from atados.atados.views import home
from haystack.views import SearchView

urlpatterns = patterns(
    '',

    url(r'^$', home, name='home'),

    url(_(r'^sign-in$'), 'django.contrib.auth.views.login',
        {'authentication_form': AuthenticationForm,
         'template_name': 'atados/atados/sign-in.html'}, name='sign-in'),

    url(r'^sign-in$', redirect_to,
        {'url': _('/sign-in'),
         'query_string': True}, name='global-sign-in'),

    url(_(r'^sign-out$'), 'django.contrib.auth.views.logout',
        {'next_page': _('/sign-in')}, name='sign-out'),

    url(_(r'^search$'), SearchView(form_class=SearchForm), name='search'),
)
