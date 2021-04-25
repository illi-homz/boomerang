from django import template

register = template.Library()


@register.filter
def get_locale(dict, key):
    return dict[key]
