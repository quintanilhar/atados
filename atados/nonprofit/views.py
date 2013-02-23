from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.utils.decorators import classonlymethod
from atados.nonprofit.models import Nonprofit
from atados.nonprofit.forms import (NonprofitPictureForm,
                                       NonprofitDetailsForm)


class NonprofitMixin(object):
    nonprofit = None
    only_owner = True

    def get_context_data(self, **kwargs):
        context = super(NonprofitMixin, self).get_context_data(**kwargs)
        context.update({'nonprofit': self.get_nonprofit()})
        return context

    def dispatch(self, request, *args, **kwargs):
        self.nonprofit = get_object_or_404(Nonprofit,
                                              slug=kwargs.get('nonprofit'))
        if self.only_owner and self.nonprofit.user != request.user:
            raise PermissionDenied
        return super(NonprofitMixin, self).dispatch(request,
                                                       *args, **kwargs)

    def get_nonprofit(self):
        return self.nonprofit

class NonprofitBaseView(NonprofitMixin, TemplateView):
    pass

class NonprofitHomeView(TemplateView):
    template_name = 'atados/nonprofit/home.html'

class NonprofitDetailsView(NonprofitBaseView):
    only_owner = False
    template_name = 'atados/nonprofit/details.html'

class NonprofitPictureUpdateView(NonprofitMixin, UpdateView):
    model = Nonprofit
    form_class=NonprofitPictureForm
    template_name='atados/nonprofit/picture.html'
    get_object = NonprofitMixin.get_nonprofit

class NonprofitDetailsUpdateView(NonprofitMixin, UpdateView):
    model = Nonprofit
    form_class=NonprofitDetailsForm
    template_name='atados/nonprofit/edit-details.html'
    get_object = NonprofitMixin.get_nonprofit
