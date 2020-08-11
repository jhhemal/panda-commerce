from django import template
register = template.Library()

@register.filter(name='inc_val')
def inc_val(val):
    val = val + 1
    return val

@register.filter(name='zero_val')
def zero_val(val):
    val = 0
    return val
