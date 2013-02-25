from django import template
from django.template import Context
from django.template.loader import get_template
from django.forms.forms import BoundField
from atados.project.models import Availability, WEEKDAYS, PERIODS
import re

register = template.Library()

@register.simple_tag
def get_availability(request, weekday_id, period_id):
    return Availability.objects.filter(weekday=weekday_id, period=period_id).get(0)

    availabilities = dict([(weekday_id, {})
        for weekday_id, weekday_label in WEEKDAYS])
    for availability in Availability.objects.all():
        availabilities[availability.weekday].update(
                {availability.period: availability.id})
    

@register.filter
def as_availabilities_field(field):
    if isinstance(field, BoundField):
        return get_template("atados/project/availabilities_field.html").render(
            Context({
                'field': field,
                'periods': PERIODS,
                'weekdays': WEEKDAYS,
            })
        )
    else:
        # Display the default
        return settings.TEMPLATE_STRING_IF_INVALID
