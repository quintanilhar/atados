from django.views.generic.simple import direct_to_template
from atados.volunteer.views import VolunteerView
from atados.volunteer.forms import RegistrationForm
from atados.organisation.views import OrganisationView
from atados.organisation.models import Organisation


template_name = 'atados/atados/home.html'

def home(request, *args, **kwargs):
    if request.user.is_authenticated():
        try:
            Organisation.objects.get(user=request.user)
            return OrganisationView.as_view()(request, *args, **kwargs)
        except Organisation.DoesNotExist:
            return VolunteerView.as_view()(request, *args, **kwargs)

    return direct_to_template(request, 'atados/atados/home.html',
                              {'form': RegistrationForm()})
