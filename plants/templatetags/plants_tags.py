from django import template
from string import capwords

register = template.Library()

@register.filter
def titleCaps(value):
    if value:
        return capwords(value)
    
    return value


@register.filter
def stripSlashes(value):
    return value.replace('/', '')


@register.simple_tag
def define(val=None):
  return val