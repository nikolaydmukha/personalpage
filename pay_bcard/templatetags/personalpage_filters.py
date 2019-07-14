from django import template
register = template.Library()


@register.filter(name='phone_number')
def phone_number(number):
    """Convert a +79991001111 string into +7(xxx)xxx-xx-xx."""
    country_code = number[0:2]
    first = number[2:5]
    print(first,"\n")
    second = number[5:8]
    third = number[8:10]
    fourth = number[10:12]
    return f'{country_code} ({first}) {second}-{third}-{fourth}'
