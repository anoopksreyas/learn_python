from django import template

register = template.Library()

@register.filter(name='square')
def square(age, name):
    print name
    return age**2

@register.inclusion_tag('countries_list.html')
def countries():
    return {}