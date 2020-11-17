from django import template
from string import capwords

register = template.Library()

@register.filter
def titleCaps(value):
    return capwords(value)


@register.filter
def stripSlashes(value):
    return value.replace('/', '')