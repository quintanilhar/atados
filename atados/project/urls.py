from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template, redirect_to
from django.utils.translation import ugettext_lazy as _
from atados.nonprofit.views import NonprofitBaseView
from atados.project.views import (ProjectDonationCreateView,
                                  ProjectWorkCreateView,
                                  ProjectJobCreateView,
                                  ProjectDetailsView, ProjectUpdateView,
                                  ProjectCollaboratorsView,
                                  ProjectDeleteView,
                                  ProjectApplyView,
                                  ProjectPictureUpdateView)

urlpatterns = patterns(
    '',

    url(_(r'^project$'), direct_to_template, {'template': 'atados/project/index.html'}, name='index'),
    url(_(r'^(?P<nonprofit>[-\w]+)/add-new-project$'), NonprofitBaseView.as_view(template_name='atados/project/project-kind-choose.html'), name='new'),
    url(_(r'^(?P<nonprofit>[-\w]+)/add-new-project/donation$'), ProjectDonationCreateView.as_view(), name='new-donation'),
    url(_(r'^(?P<nonprofit>[-\w]+)/add-new-project/work$'), ProjectWorkCreateView.as_view(), name='new-work'),
    url(_(r'^(?P<nonprofit>[-\w]+)/add-new-project/job$'), ProjectJobCreateView.as_view(), name='new-job'),
    url(_(r'^(?P<nonprofit>[-\w]+)/(?P<project>[-\w]+)$'), ProjectDetailsView.as_view(), name='details'),
    url(_(r'^(?P<nonprofit>[-\w]+)/(?P<project>[-\w]+)/edit$'), ProjectUpdateView.as_view(), name='edit'),
    url(_(r'^(?P<nonprofit>[-\w]+)/(?P<project>[-\w]+)/collaborators$'), ProjectCollaboratorsView.as_view(), name='collaborators'),
    url(_(r'^(?P<nonprofit>[-\w]+)/(?P<project>[-\w]+)/delete$'), ProjectDeleteView.as_view(), name='delete'),
    url(_(r'^(?P<nonprofit>[-\w]+)/(?P<project>[-\w]+)/apply$'), ProjectApplyView.as_view(), name='apply'),

    url(_(r'^(?P<nonprofit>[-\w]+)/(?P<project>[-\w]+)/picture$'), ProjectPictureUpdateView.as_view(),
        name='edit-project-picture'),
)
