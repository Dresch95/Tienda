from django import template
register = template.Library()

@register.filter
def product(value, product):
    return round(value * product, 2)