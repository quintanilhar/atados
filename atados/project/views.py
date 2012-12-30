from django.views.generic.edit import CreateView, ModelFormMixin
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from atados.project.models import Project
from atados.organisation.models import Organisation
from atados.organisation.views import OrganisationMixin
from atados.project.forms import ProjectCreateForm


class ProjectMixin(OrganisationMixin):
    project = None

    def get_context_data(self, **kwargs):
        context = super(ProjectMixin, self).get_context_data(**kwargs)
        context.update({'project': self.get_project()})
        return context

    def get_project(self):
        if self.project is None:
            self.project = get_object_or_404(Project,
                                             organisation=self.get_organisation(),
                                             slug=self.kwargs.get('project'))
        return self.organisation

class ProjectCreateView(OrganisationMixin, CreateView):
    model=Project
    form_class=ProjectCreateForm
    template_name='atados/project/new.html'

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        kwargs.update({
            'organisation': self.get_organisation(),
        })
        return kwargs

    def form_valid(self, form):
        model = form.save(commit=False)
        if self.request.user.is_authenticated():
            model.organisation = Organisation.objects.get(user=self.request.user)
        return super(ProjectCreateView, self).form_valid(form)

class ProjectView(DetailView, ProjectMixin):
    model=Project
    form_class=ProjectCreateForm
    template_name='atados/project/view.html'

    def get_queryset(self):
        return self.get_project()
