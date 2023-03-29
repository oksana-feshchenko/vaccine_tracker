from django import template

register = template.Library()


@register.simple_tag
def whole_division(value: str, divider: str):
    value = int(value)
    divider = int(divider)
    return value // divider
