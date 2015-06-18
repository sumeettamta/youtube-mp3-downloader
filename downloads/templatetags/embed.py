from django import template

register = template.Library()

@register.filter(name='embed')
def embed(value):
    return value.replace('watch?v=', 'embed/') + '?rel=0'