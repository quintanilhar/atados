from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.organisation.views import OrganisationBaseView
from atados.project.views import (ProjectDonationCreateView,
                                  ProjectJustOnceCreateView,
                                  ProjectPeriodicCreateView, ProjectView,
                                  ProjectEditView, ProjectCollaboratorsView,
                                  ProjectRequestsView, ProjectStepsView)

urlpatterns = patterns(
    '',

    url(_(r'^project$'), direct_to_template, {'template': 'atados/project/index.html'}, name='index'),
    url(_(r'^(?P<organisation>[-\w]+)/add-new-project$'), OrganisationBaseView.as_view(template_name='atados/project/project-kind-choose.html'), name='new'),
    url(_(r'^(?P<organisation>[-\w]+)/add-new-project/donation$'), ProjectDonationCreateView.as_view(), name='new-donation'),
    url(_(r'^(?P<organisation>[-\w]+)/add-new-project/just-once$'), ProjectJustOnceCreateView.as_view(), name='new-just-once'),
    url(_(r'^(?P<organisation>[-\w]+)/add-new-project/periodic$'), ProjectPeriodicCreateView.as_view(), name='new-periodic'),
    url(_(r'^(?P<organisation>[-\w]+)/(?P<project>[-\w]+)$'), ProjectView.as_view(), name='view'),
    url(_(r'^(?P<organisation>[-\w]+)/(?P<project>[-\w]+)/edit$'), ProjectEditView.as_view(), name='edit'),
    url(_(r'^(?P<organisation>[-\w]+)/(?P<project>[-\w]+)/collaborators$'), ProjectCollaboratorsView.as_view(), name='collaborators'),
    url(_(r'^(?P<organisation>[-\w]+)/(?P<project>[-\w]+)/requests$'), ProjectRequestsView.as_view(), name='requests'),
    url(_(r'^(?P<organisation>[-\w]+)/(?P<project>[-\w]+)/steps$'), ProjectStepsView.as_view(), name='steps'),
)
