from django.db import models
from django.utils.translation import ugettext_lazy as _
from atados.organisation.models import Organisation
from atados.volunteer.models import Volunteer
from sorl.thumbnail import ImageField
from time import time

WEEKDAYS = (
        (0, _('Sunday')),
        (1, _('Monday')),
        (2, _('Sunday')),
        (3, _('Sunday')),
        (4, _('Sunday')),
        (5, _('Sunday')),
        (6, _('Sunday')),
)

class Disponibility(models.Model):
    weekday = models.PositiveSmallIntegerField(_('weekday'))
    hour = models.PositiveSmallIntegerField(_('hour'))

    def __unicode__(self):
        return '% as %' % self.weekday, self.hour

class Cause(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    organisation = models.ForeignKey(Organisation)
    cause = models.ManyToManyField(Cause)
    disponibility = models.ManyToManyField(Disponibility)
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
    vacancies = models.PositiveSmallIntegerField(_('Vacancies'),
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
    skill = models.ManyToManyField(Skill)
    weekly_hours = models.PositiveSmallIntegerField(_('Weekly hours'),
                                        blank=True, null=True)
    can_be_done_remotely = models.BooleanField(
            _('This work can be done remotely.'))

class Apply(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    project = models.ForeignKey(Project)
