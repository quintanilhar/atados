from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, ModelFormMixin, UpdateView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify
from atados.project.models import Project, ProjectDonation, ProjectWork
from atados.organisation.models import Organisation
from atados.organisation.views import OrganisationMixin
from atados.project.forms import (ProjectDonationCreateForm,
                                  ProjectJustOnceCreateForm,
                                  ProjectPeriodicCreateForm)


class ProjectMixin(OrganisationMixin):
    project = None

    def get_context_data(self, **kwargs):
        context = super(ProjectMixin, self).get_context_data(**kwargs)
        context.update({'project': self.get_project()})
        return context

    def get_project(self):
        if self.project is None:
            try:
                self.project = ProjectWork.objects.get(
                    organisation=self.get_organisation(),
                    slug=self.kwargs.get('project'))
            except ProjectWork.DoesNotExist:
                try:
                    self.project = ProjectDonation.objects.get(
                        organisation=self.get_organisation(),
                        slug=self.kwargs.get('project'))
                except ProjectDonation.DoesNotExist:
                    raise Http404

        return self.project

    get_object = get_project

class ProjectCreateView(OrganisationMixin, CreateView):
    model=Project

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
            model.slug = slugify(model.name)
        else:
            forms.ValidationError("Authentication required")
        return super(ProjectCreateView, self).form_valid(form)

class ProjectDonationCreateView(ProjectCreateView):
    form_class=ProjectDonationCreateForm
    template_name='atados/project/new-donation.html'

class ProjectJustOnceCreateView(ProjectCreateView):
    form_class=ProjectJustOnceCreateForm
    template_name='atados/project/new-work.html'

class ProjectPeriodicCreateView(ProjectJustOnceCreateView):
    form_class=ProjectPeriodicCreateForm
    template_name='atados/project/new-periodic.html'

class ProjectDetailsView(ProjectMixin, DetailView):
    only_owner=False

    def get_template_names(self):
        if isinstance(self.object, ProjectDonation):
            return 'atados/project/details-donation.html'
        if isinstance(self.object, ProjectWork):
            if self.object.monthly_hours > 0:
                return 'atados/project/details-periodic.html'
            else:
                return 'atados/project/details-work.html'
        return 'atados/project/details.html'


class ProjectEditView(ProjectMixin, UpdateView):
    model=Project
    form_class=ProjectDonationCreateForm
    template_name='atados/project/edit.html'

    def get_form_kwargs(self):
        kwargs = super(ProjectEditView, self).get_form_kwargs()
        kwargs.update({
            'organisation': self.get_organisation(),
        })
        return kwargs

    def get_success_url(self):
        return reverse('project:edit',
                       args=[self.object.organisation.slug, self.object.slug])

    def form_valid(self, form):
        model = form.save(commit=False)
        if self.request.user.is_authenticated():
            model.organisation = Organisation.objects.get(user=self.request.user)
            model.slug = slugify(model.name)
        else:
            forms.ValidationError("Authentication required")
        return super(ProjectEditView, self).form_valid(form)

class ProjectCollaboratorsView(ProjectMixin, TemplateView):
    template_name = 'atados/project/collaborators.html'

class ProjectRequestsView(ProjectMixin, TemplateView):
    template_name = 'atados/project/requests.html'

class ProjectStepsView(ProjectMixin, TemplateView):
    template_name = 'atados/project/steps.html'
