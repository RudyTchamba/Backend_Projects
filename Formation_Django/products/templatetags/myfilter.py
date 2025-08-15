from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='addcent')
def addcent(value):
    return value + 100000


@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of arg from the given string
    """
    return value.replace(arg, 'xxxx')

@register.filter(name='lowercase')
@stringfilter
def lower(value):
    return value.upper()