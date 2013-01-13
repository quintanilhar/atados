from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from django.utils.decorators import classonlymethod
from atados.volunteer.models import Volunteer
from atados.volunteer.forms import VolunteerPictureForm


class UserReferenceMixin(object):
    only_owner = True
    user = None

    def get_context_data(self, **kwargs):
        context = super(UserReferenceMixin, self).get_context_data(**kwargs)
        context.update({'user_reference': self.get_user_reference()})
        return context

    def dispatch(self, request, *args, **kwargs):
        if self.only_owner and request.user.username != kwargs.get('username'):
            raise Http404
        return super(UserReferenceMixin, self).dispatch(request,
                                                        *args, **kwargs)
 
    def get_user_reference(self):
        if self.user is None:
            self.user = get_object_or_404(User,
                                          username=self.kwargs.get('username'))
        return self.user

class VolunteerMixin(UserReferenceMixin):
    volunteer = None
    only_owner = True

    def get_context_data(self, **kwargs):
        context = super(VolunteerMixin, self).get_context_data(**kwargs)
        context.update({'volunteer': self.get_volunteer()})
        return context

    def dispatch(self, request, *args, **kwargs):
        self.kwargs = kwargs
        self.volunteer = get_object_or_404(Volunteer,
                                           user=self.get_user_reference())
        if self.only_owner and self.volunteer.user != request.user:
            raise PermissionDenied
        return super(VolunteerMixin, self).dispatch(request,
                                                    *args, **kwargs)

    def get_volunteer(self):
        return self.volunteer

class VolunteerBaseView(VolunteerMixin, TemplateView):
    pass

class VolunteerHomeView(TemplateView):
    template_name = 'atados/volunteer/home.html'

class VolunteerDetailsView(VolunteerBaseView):
    only_owner = False
    template_name = 'atados/volunteer/details.html'

class VolunteerPictureUpdateView(VolunteerMixin, UpdateView):
    model = Volunteer
    form_class=VolunteerPictureForm
    template_name='atados/volunteer/picture.html'
    get_object = VolunteerMixin.get_volunteer
