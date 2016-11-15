# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from functools import partial

__version_info__ = '0.1.0'
__version__ = '0.1.0'
version = '0.1.0'
VERSION = '0.1.0'
__all__ = ['get_version', 'generate_css_names_from_string',
           'request_path_to_css_names']

def get_version():
    return version  # pragma: no cover


def generate_css_names_from_string(item, split_on, prefix='', suffix='', midpoint=''):
    newpath = item.strip(split_on).split(split_on)
    newpath_length = len(newpath) + 1
    variations = (newpath[0:l] for l in range(1, newpath_length))
    # If there's a prefix and it doesn't end with a sensible separator (given
    # the valid names of CSS identifiers), add midpoint.
    if prefix and not prefix.endswith(('-', '_')):
        prefix = '%s%s' % (prefix, midpoint)
    # same as prefix, but start, rather than end
    if suffix and not suffix.startswith(('-', '_')):
        suffix = '%s%s' % (midpoint, suffix,)

    finalised_variations = (
        '%s%s%s' % (prefix, midpoint.join(variation), suffix)
        for variation in variations
    )
    return finalised_variations


request_path_to_css_names = partial(generate_css_names_from_string,
                                    split_on='/')
