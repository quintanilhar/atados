from django.db import models
from django.utils.translation import ugettext_lazy as _
from atados.organisation.models import Organisation
from atados.volunteer.models import Volunteer


class Classification(models.Model):
    name = models.CharField(_('name'), max_length=30)

    def __unicode__(self):
        return self.name

class Project(models.Model):
    organisation = models.ForeignKey(Organisation)
    name = models.CharField(_('Project name'), max_length=50)
    slug = models.SlugField(max_length=50)
    details = models.TextField(_('Details'), max_length=1024)
    responsible = models.CharField(_('Responsible name'), max_length=50)
    phone = models.CharField(_('Phone'), max_length=20)
    email = models.EmailField(_('E-mail address'))
    addressline = models.CharField(_('Address line'), max_length=200,
                                  blank=True, null=True, default=None)
    neighborhood = models.CharField(_('Neighborhood'), max_length=50,
                                    blank=True, null=True, default=None)
    city = models.CharField(_('City'), max_length=50,
                            blank=True, null=True, default=None)

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

class ProjectDonation(Project):
    collection_by_organisation = models.BooleanField(
            _('Collection made by the organisation'))
    delivery_by_donor = models.BooleanField(
            _('Delivery made by donor'))

class ProjectWork(Project):
    classification = models.ForeignKey(Classification)
    monthly_hours = models.IntegerField(_('Monthly hours (approximate)'),
                                        blank=True, null=True)
    can_be_done_remotely = models.BooleanField(
            _('This work can be done remotely.'))
