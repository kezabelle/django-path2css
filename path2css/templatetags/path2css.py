# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
try:
    from collections import UserList
except ImportError:
    from UserList import UserList

from django import template
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.safestring import mark_safe
from path2css import request_path_to_css_names
register = template.Library()


@python_2_unicode_compatible
class Output(UserList):
    def __str__(self):
        """
        Used when doing something like:
        {% path2css ... as OUTVAR %}
        {{ OUTVAR }}
        """
        return mark_safe(" ".join(force_text(x) for x in self.data))

    def __html__(self):
        """
        Used in {% path2css x y %} is used directly
        """
        return force_text(self)

    def __getitem__(self, item):
        """
        Used when doing something like:
        {% path2css ... as OUTVAR %}
        {% for x in OUTVAR %}{{ x }}{% endfor %}
        """
        return mark_safe(super(Output, self).__getitem__(item))


@register.simple_tag(takes_context=False)
def path2css(path, prefix='', suffix='', midpoint='-'):
    variations = request_path_to_css_names(item=path, prefix=prefix, suffix=suffix,
                                           midpoint=midpoint)
    return Output(variations)
