from django import template
register = template.Library()

@register.filter()
def lookup(lst, value):
    return lst[value]

@register.filter()
def kToC(value):
    return "{:.2f}".format(value - 273.15)

@register.filter()
def split_str(str):
    return str.split(" ")