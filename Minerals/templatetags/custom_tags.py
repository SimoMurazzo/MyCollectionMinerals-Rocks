from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def keep_query_params(context, **kwargs):
    query = context['request'].GET.copy()
    for k, v in kwargs.items():
        query[k] = v
    return f'?{query.urlencode()}'
