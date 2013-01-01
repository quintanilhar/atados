from django.http import Http404
from django.views.generic.simple import direct_to_template
from django.contrib.auth.models import User
from atados.volunteer.views import VolunteerView, VolunteerHomeView
from atados.volunteer.forms import RegistrationForm
from atados.organisation.views import OrganisationView, OrganisationHomeView
from atados.organisation.models import Organisation


template_name = 'atados/atados/home.html'

def home(request, *args, **kwargs):
    if request.user.is_authenticated():
        try:
            Organisation.objects.get(user=request.user)
            return OrganisationHomeView.as_view()(request, *args, **kwargs)
        except Organisation.DoesNotExist:
            return VolunteerHomeView.as_view()(request, *args, **kwargs)

    return direct_to_template(request, 'atados/atados/home.html',
                              {'form': RegistrationForm()})

def slug(request, *args, **kwargs):
    try:
        User.objects.get(username=kwargs['slug'])
        kwargs.update({
            'username': kwargs.pop('slug')
        })
        return VolunteerView.as_view()(request, *args, **kwargs)
    except User.DoesNotExist:
        try:
            Organisation.objects.get(slug=kwargs['slug'])
            kwargs.update({
                'organisation': kwargs.pop('slug')
            })
            return OrganisationView.as_view()(request, *args, **kwargs)
        except Organisation.DoesNotExist:
            raise Http404
