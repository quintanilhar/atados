from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Profile(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(_('address'), max_length=100, blank=True)
    number = models.CharField(_('number'), max_length=9, blank=True)

    def image_name(self, filename):
        left_path, extension = filename.rsplit('.', 1)
        return 'profile/%s.%s' % (self.id, extension)

    image = ImageField(upload_to=image_name, blank=True)
