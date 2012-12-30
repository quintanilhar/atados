from django.views.generic import TemplateView
from django.utils.decorators import classonlymethod


class VolunteerView(TemplateView):
    template_name = 'atados/volunteer/home.html'
