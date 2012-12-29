from django.views.generic.edit import CreateView, ModelFormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required, login_required
from django.template.defaultfilters import slugify
from atados.project.models import Project
from atados.organisation.models import Organisation
from atados.project.forms import ProjectCreateForm


class OrganisationMixin(ModelFormMixin):

    def form_valid(self, form):
        model = form.save(commit=False)
        if self.request.user.is_authenticated():
            model.organisation = Organisation.objects.get(user=self.request.user)
        return super(OrganisationMixin, self).form_valid(form)

    @method_decorator(login_required)
    @method_decorator(permission_required('add_project', raise_exception=True))
    def dispatch(self, request, *args, **kwargs):
        return super(OrganisationMixin, self).dispatch(request, *args, **kwargs)

class SlugifyNameMixin(ModelFormMixin):

    def form_valid(self, form):
        model = form.save(commit=False)
        model.slug = slugify(model.name)
        return super(SlugifyNameMixin, self).form_valid(form)

class CreateProjectView(CreateView, OrganisationMixin, SlugifyNameMixin):
    model=Project
    form_class=ProjectCreateForm
    template_name='atados/project/new.html'
    success_url=''
