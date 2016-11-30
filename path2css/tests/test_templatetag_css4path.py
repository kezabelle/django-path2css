# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import django
import pytest
from django.conf import settings
from django.template import Context, Template as T

CTX = Context()

def test_templatetag():
    resp = T('{% load path2css %}{% css4path "/test/path/" %}').render(CTX).strip()
    expected = '<link href="{}css/test-path.css" rel="stylesheet" type="text/css" />'.format(settings.STATIC_URL)
    assert resp == expected

def test_templatetag_root_does_nothing():
    resp = T('{% load path2css %}{% css4path "//" %}').render(CTX).strip()
    assert resp == ''


def test_templatetag_with_prefix():
    resp = T('{% load path2css %}{% css4path "/test/" prefix="HELLO" %}').render(
        CTX,
    ).strip()
    expected = '<link href="{}css/HELLO-test.css" rel="stylesheet" type="text/css" />'.format(settings.STATIC_URL)
    assert resp == expected


def test_templatetag_with_prefix_ending_with_separator():
    resp = T('{% load path2css %}{% css4path "/test/" prefix="HELLO_" %}').render(
        CTX,
    ).strip()
    expected = '<link href="{}css/HELLO_test.css" rel="stylesheet" type="text/css" />'.format(settings.STATIC_URL)
    assert resp == expected


def test_templatetag_with_suffix():
    resp = T('{% load path2css %}{% css4path "/test/" suffix="BYE" %}').render(
        CTX,
    ).strip()
    expected = '<link href="{}css/test-BYE.css" rel="stylesheet" type="text/css" />'.format(settings.STATIC_URL)
    assert resp == expected

def test_templatetag_with_suffix_ending_with_separator():
    resp = T('{% load path2css %}{% css4path "/test/" suffix="_BYE" %}').render(
        CTX,
    ).strip()
    expected = '<link href="{}css/test_BYE.css" rel="stylesheet" type="text/css" />'.format(settings.STATIC_URL)
    assert resp == expected


@pytest.mark.xfail(condition=django.VERSION[0:2] < (1, 9),
                   reason="Django 1.8 doesn't have combination simple/assignment tags")
def test_templatetag_assignment():
    resp = T('''{% load path2css %}{% css4path "/test/path/" as GOOSE %}
    before ... {% for part in GOOSE %}-{{part}}-{% endfor %} ... after
    ''').render(
        CTX,
    ).strip()
    parts = [x for x in resp.split() if x]
    assert parts == ['before', '...', '-/__static__/css/test-path.css-', '...', 'after']
