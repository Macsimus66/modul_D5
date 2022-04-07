from django import template

register = template.Library()

BAD_WORDS = ['мать', 'твою', 'тудыть']


@register.filter(name='Censor')
def Censor(value):
    for word in BAD_WORDS:
        value = value.replace(word[0:], '*' * (len(word) - 1))

    return value


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
        return d.urlencode()