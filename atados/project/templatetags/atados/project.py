from django import template
from django.template import Context
from django.template.loader import get_template
from atados.project.models import Availability, WEEKDAYS, PERIODS
import re


register = template.Library()

@register.filter
def as_availabilities_field(field):
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

@register.filter
def as_causes_field(field):
    return get_template("atados/project/causes_field.html").render(
        Context({
            'field': field,
        })
    )

@register.filter
def as_skills_field(field):
    return get_template("atados/project/skills_field.html").render(
        Context({
            'field': field,
        })
    )
