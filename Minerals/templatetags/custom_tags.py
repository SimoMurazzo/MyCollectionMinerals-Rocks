from django import template

from Minerals.models import remove_exponent

register = template.Library()


@register.simple_tag(takes_context=True)
def keep_query_params(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return f'?{query.urlencode()}'


@register.filter
def to_ct(value):
    return value * 5


@register.filter
def remove_exponent_tag(value):
    return remove_exponent(value)
