from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField
from time import time


class Nonprofit(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(_('Name'), max_length=50)
    slug = models.SlugField(max_length=50)
    details = models.TextField(_('Details'), max_length=1024, blank=True,
                               null=True, default=None)

    def image_name(self, filename):
        left_path, extension = filename.rsplit('.', 1)
        return 'nonprofit/%s/%s.%s' % (time(), self.slug, extension)

    image = ImageField(upload_to=image_name, blank=True,
                       null=True, default=None)

    @models.permalink
    def get_absolute_url(self):
        return ('slug', (self.slug,))

    def __unicode__(self):
        return self.name
