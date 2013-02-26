from django import template
import re

register = template.Library()

@register.simple_tag
def active(request, href):
    if re.search(href, request.path):
        return 'active'
    return ''
