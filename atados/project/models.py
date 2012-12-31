from django.db import models
from django.utils.translation import ugettext_lazy as _
from atados.organisation.models import Organisation
from atados.volunteer.models import Volunteer


class Project(models.Model):
    organisation = models.ForeignKey(Organisation)
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(max_length=50)
    details = models.TextField(_('details'), max_length=500)
    where = models.CharField(_('Where'), max_length=100)
    when = models.CharField(_('When'), max_length=30)
    how_long = models.CharField(_('How long'), max_length=30)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('project:view', (self.organisation.slug, self.slug))

    @models.permalink
    def get_edit_url(self):
        return ('project:edit', (self.organisation.slug, self.slug))

    class Meta:
        unique_together = (("slug", "organisation"),)

class Step(models.Model):
    project = models.ForeignKey(Project)
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(max_length=50)

class Request(models.Model):
    step = models.ForeignKey(Step)
    volunteer = models.ForeignKey(Volunteer)
    create_time = models.DateTimeField(True)
