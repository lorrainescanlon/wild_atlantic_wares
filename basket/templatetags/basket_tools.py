from django import template

register = template.Library()


@register.filter(name='calc_linetotal')
def calc_linetotal(price, quantity):
    return price * quantity
