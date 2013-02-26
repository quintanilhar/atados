from django import template
from django.conf import settings
from django.template import Context
from django.template.loader import get_template
from django.forms.forms import BoundField
from atados.project.models import Availability, WEEKDAYS, PERIODS
import re


register = template.Library()

@register.filter
def as_availabilities_field(field):
    if isinstance(field, BoundField):
        availabilities = dict([(weekday_id, {'weekday_label': weekday_label, 'periods': {}})
            for weekday_id, weekday_label in WEEKDAYS])
        for availability in Availability.objects.all():
            availabilities[availability.weekday]['periods'].update(
                    {availability.period: availability.id})

        print availabilities
        return get_template("atados/project/availabilities_field.html").render(
            Context({
                'field': field,
                'availabilities': availabilities,
                'periods': PERIODS,
                'weekdays': WEEKDAYS,
            })
        )
    else:
        # Display the default
        return settings.TEMPLATE_STRING_IF_INVALID

@register.filter
def as_causes_field(field):
    return settings.TEMPLATE_STRING_IF_INVALID

@register.filter
def as_skills_field(field):
    return settings.TEMPLATE_STRING_IF_INVALID
