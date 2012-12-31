from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
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
        return self.project

    get_object = get_project

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

class ProjectView(ProjectMixin, DetailView):
    model=Project
    only_owner=False
    form_class=ProjectCreateForm
    template_name='atados/project/view.html'

class ProjectEditView(ProjectMixin, UpdateView):
    model=Project
    form_class=ProjectCreateForm
    template_name='atados/project/edit.html'

    def get_success_url(self):
        return reverse('project:edit',
                       args=[self.object.organisation.slug, self.object.slug])

    def get_form_kwargs(self):
        kwargs = super(ProjectEditView, self).get_form_kwargs()
        kwargs.update({
            'organisation': self.get_organisation(),
        })
        return kwargs

    def form_valid(self, form):
        model = form.save(commit=False)
        if self.request.user.is_authenticated():
            model.organisation = Organisation.objects.get(user=self.request.user)
        return super(ProjectEditView, self).form_valid(form)

class ProjectCollaboratorsView(ProjectMixin, TemplateView):
    template_name = 'atados/project/collaborators.html'

class ProjectRequestsView(ProjectMixin, TemplateView):
    template_name = 'atados/project/requests.html'

class ProjectStepsView(ProjectMixin, TemplateView):
    template_name = 'atados/project/steps.html'
