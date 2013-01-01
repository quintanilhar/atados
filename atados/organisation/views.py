from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.utils.decorators import classonlymethod
from atados.organisation.models import Organisation


class OrganisationMixin(object):
    organisation = None
    only_owner = True

    def get_context_data(self, **kwargs):
        context = super(OrganisationMixin, self).get_context_data(**kwargs)
        context.update({'organisation': self.get_organisation()})
        return context

    def dispatch(self, request, *args, **kwargs):
        self.organisation = get_object_or_404(Organisation,
                                              slug=kwargs.get('organisation'))
        if self.only_owner and self.organisation.user != request.user:
            raise PermissionDenied
        return super(OrganisationMixin, self).dispatch(request,
                                                       *args, **kwargs)

    def get_organisation(self):
        return self.organisation

class OrganisationBaseView(OrganisationMixin, TemplateView):
    pass

class OrganisationHomeView(TemplateView):
    template_name = 'atados/organisation/home.html'

class OrganisationView(OrganisationBaseView):
    only_owner = False
    template_name = 'atados/organisation/view.html'
