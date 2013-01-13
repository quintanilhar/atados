from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from time import time


class Volunteer(models.Model):
    user = models.ForeignKey(User)

    def image_name(self, filename):
        left_path, extension = filename.rsplit('.', 1)
        return 'volunteer/%s/%s.%s' % (time(), self.user.username, extension)

    image = ImageField(upload_to=image_name, blank=True,
                       null=True, default=None)

    @models.permalink
    def get_absolute_url(self):
        return ('slug', (self.user.username,))

    def __unicode__(self):
        return self.user.first_name

