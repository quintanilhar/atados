from django.db import models
from django.utils.translation import ugettext_lazy as _
from atados.organisation.models import Organisation


class Project(models.Model):
    organisation = models.ForeignKey(Organisation)
    name = models.CharField(_('name'), max_length=50)
    slug = models.SlugField(max_length=50)

    def __unicode__(self):
        return self.name
