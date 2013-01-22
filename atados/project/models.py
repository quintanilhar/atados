from django.db import models
from django.utils.translation import ugettext_lazy as _
from atados.organisation.models import Organisation
from atados.volunteer.models import Volunteer
from sorl.thumbnail import ImageField
from time import time


class Classification(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    organisation = models.ForeignKey(Organisation)
    name = models.CharField(_('Project name'), max_length=50)
    slug = models.SlugField(max_length=50)
    details = models.TextField(_('Details'), max_length=1024)
    prerequisites = models.TextField(_('Prerequisites'), max_length=1024)
    responsible = models.CharField(_('Responsible name'), max_length=50)
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(_('E-mail address'))
    zipcode = models.CharField(_('Zip code'), max_length=10,
                               blank=True, null=True, default=None)
    addressline = models.CharField(_('Address line'), max_length=200,
                                  blank=True, null=True, default=None)
    neighborhood = models.CharField(_('Neighborhood'), max_length=50,
                                    blank=True, null=True, default=None)
    city = models.CharField(_('City'), max_length=50,
                            blank=True, null=True, default=None)
    vacancies = models.IntegerField(_('Vacancies'),
                                    blank=True, null=True, default=None)

    def image_name(self, filename):
        left_path, extension = filename.rsplit('.', 1)
        return 'project/%s/%s/%s.%s' % (self.organisation.slug,
                                        time(), self.slug, extension)

    image = ImageField(upload_to=image_name, blank=True,
                       null=True, default=None)

    def __unicode__(self):
        return  '%s - %s' % (self.name, self.organisation.name)

    @models.permalink
    def get_absolute_url(self):
        return ('project:details', (self.organisation.slug, self.slug))

    @models.permalink
    def get_edit_url(self):
        return ('project:edit', (self.organisation.slug, self.slug))

    class Meta:
        unique_together = (("slug", "organisation"),)

class ProjectDonation(Project):
    collection_by_organisation = models.BooleanField(
            _('Collection made by the organisation'))

class ProjectWork(Project):
    classification = models.ForeignKey(Classification)
    weekly_hours = models.IntegerField(_('Weekly hours (approximate)'),
                                        blank=True, null=True)
    can_be_done_remotely = models.BooleanField(
            _('This work can be done remotely.'))

class Apply(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    project = models.ForeignKey(Project)
