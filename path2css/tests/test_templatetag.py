# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.template import Context, Template as T

CTX = Context()

def test_templatetag():
    resp = T('{% load path2css %}{% path2css "/test/path/" %}').render(CTX).strip()
    assert resp == 'test test-path'

def test_templatetag_root_does_nothing():
    resp = T('{% load path2css %}{% path2css "//" %}').render(CTX).strip()
    assert resp == ''


def test_templatetag_with_prefix():
    resp = T('{% load path2css %}{% path2css "/test/" prefix="HELLO" %}').render(
        CTX,
    ).strip()
    assert resp == 'HELLO-test'


def test_templatetag_with_prefix_ending_with_separator():
    resp = T('{% load path2css %}{% path2css "/test/" prefix="HELLO_" %}').render(
        CTX,
    ).strip()
    assert resp == 'HELLO_test'


def test_templatetag_with_suffix():
    resp = T('{% load path2css %}{% path2css "/test/" suffix="BYE" %}').render(
        CTX,
    ).strip()
    assert resp == 'test-BYE'

def test_templatetag_with_suffix_ending_with_separator():
    resp = T('{% load path2css %}{% path2css "/test/" suffix="_BYE" %}').render(
        CTX,
    ).strip()
    assert resp == 'test_BYE'


def test_templatetag_assignment():
    resp = T('''{% load path2css %}{% path2css "/test/" as GOOSE %}
    {% for part in GOOSE %}---{{part}}---{% endfor %}
    ''').render(
        CTX,
    ).strip()
    assert resp == '---test---'
