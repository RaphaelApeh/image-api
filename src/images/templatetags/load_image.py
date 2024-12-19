from django import template

register = template.Library()

@register.simple_tag
def images(cls):
    print(cls)