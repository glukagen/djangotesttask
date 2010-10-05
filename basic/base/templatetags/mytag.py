from django import template
from django.core.urlresolvers import reverse
from django.contrib import admin
register = template.Library()


@register.simple_tag
def get_url(o):
    return '<a href="/admin/%s/%s/%s">%s</a>' % (
        o.__class__._meta.app_label, o.__class__._meta.module_name, o.pk, o)
