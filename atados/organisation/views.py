from django.views.generic import TemplateView
from django.utils.decorators import classonlymethod


class OrganisationView(TemplateView):
    template_name = 'atados/organisation/home.html'
