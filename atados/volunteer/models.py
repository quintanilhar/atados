from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class Volunteer(models.Model):
    user = models.ForeignKey(User)
