from django.db import models
from django.utils.translation import ugettext_lazy as _
from atados.nonprofit.models import Nonprofit
from atados.volunteer.models import Volunteer
from sorl.thumbnail import ImageField
from time import time
from datetime import datetime


WEEKDAYS = (
        (1, _('Monday')),
        (2, _('Tuesday')),
        (3, _('Wednesday')),
        (4, _('Thursday')),
        (5, _('Friday')),
        (6, _('Saturday')),
        (0, _('Sunday')),
)

PERIODS = (
        (0, _('Morning')),
        (1, _('Afternoon')),
        (2, _('Evening')),
)

class Availability(models.Model):
    weekday = models.PositiveSmallIntegerField(_('weekday'), choices=WEEKDAYS)
    period = models.PositiveSmallIntegerField(_('period'), choices=PERIODS)

    def __unicode__(self):
        return _('%s at %s') % (self.get_weekday_display(), self.get_period_display())

class Cause(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name

class ProjectManager(models.Manager):
    use_for_related_fields = True

    def active(self):
        return self.get_query_set().filter(deleted=False)

    def published(self):
        return self.get_query_set().active(published=True)

class Project(models.Model):
    objects = ProjectManager()
    nonprofit = models.ForeignKey(Nonprofit)
    causes = models.ManyToManyField(Cause)
    name = models.CharField(_('Project name'), max_length=50)
    slug = models.SlugField(max_length=50)
    details = models.TextField(_('Details'), max_length=1024)
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
    published = models.BooleanField(_("Published"), default=False)
    deleted = models.BooleanField(_("Deleted"), default=False)
    deleted_date = models.DateTimeField(_("Deleted date"), blank=True,
                                        null=True)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.deleted_date = datetime.now()
        self.save()

    def image_name(self, filename):
        left_path, extension = filename.rsplit('.', 1)
        return 'project/%s/%s/%s.%s' % (self.nonprofit.slug,
                                        time(), self.slug, extension)

    image = ImageField(upload_to=image_name, blank=True,
                       null=True, default=None)

    def __unicode__(self):
        return  '%s - %s' % (self.name, self.nonprofit.name)

    @models.permalink
    def get_absolute_url(self):
        return ('project:details', (self.nonprofit.slug, self.slug))

    @models.permalink
    def get_edit_url(self):
        return ('project:edit', (self.nonprofit.slug, self.slug))

    @models.permalink
    def get_delete_url(self):
        return ('project:delete', (self.nonprofit.slug, self.slug))

    def get_project_type(self):
        return self.project_type

    class Meta:
        unique_together = (("slug", "nonprofit"),)

class ProjectDonation(Project):
    objects = ProjectManager()
    project_type = 'donation'
    collection_by_nonprofit = models.BooleanField(
            _('Collection made by the nonprofit'))

class ProjectWork(Project):
    objects = ProjectManager()
    project_type = 'work'
    availabilities = models.ManyToManyField(Availability)
    prerequisites = models.TextField(_('Prerequisites'), max_length=1024)
    skills = models.ManyToManyField(Skill)
    weekly_hours = models.PositiveSmallIntegerField(_('Weekly hours'),
                                        blank=True, null=True)
    can_be_done_remotely = models.BooleanField(
            _('This work can be done remotely.'))

class ProjectJob(ProjectWork):
    objects = ProjectManager()
    project_type = 'job'

class Apply(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    project = models.ForeignKey(Project)
