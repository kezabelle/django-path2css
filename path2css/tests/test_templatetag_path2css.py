# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import django
import pytest
from django.template import Context, Template as T

CTX = Context()


TEMPLATES = (
    ('{% load path2css %}{% path2css "/test/path/" %}', 'test test-path'),
    ('{% load path2css %}{% path2css "//" %}', ''),
    ('{% load path2css %}{% path2css "/test/" prefix="HELLO" %}', 'HELLO-test'),
    ('{% load path2css %}{% path2css "/test/" prefix="HELLO_" %}', 'HELLO_test'),
    ('{% load path2css %}{% path2css "/test/" suffix="BYE" %}', 'test-BYE'),
    ('{% load path2css %}{% path2css "/test/" suffix="_BYE" %}', 'test_BYE'),
    # testing with different separators...
    ('{% load path2css %}{% path2css "this:is:a_test" split_on=":" %}', 'this this-is this-is-a_test'),
    ('{% load path2css %}{% path2css "this$£$is$£$a_test" split_on="$£$" %}', 'this this-is this-is-a_test'),
    # Tests with more interesting/exotic/bad request strings (see #2)
    ('{% load path2css %}{% path2css "/test/…" %}', 'test'),
    ('{% load path2css %}{% path2css "/test/%E2%80%A6" %}', 'test'),
    ('{% load path2css %}{% path2css "/test/%E2%80%A6/test2.html" %}', 'test test-test2.html'),
    ('{% load path2css %}{% path2css "/test/ÅÍÎÏ˝ÓÔÒÚÆ☃" %}', 'test'),
    ('{% load path2css %}{% path2css "/test/部落格/" %}', 'test'),
    ('{% load path2css %}{% path2css "/test𝐥𝐚𝐳𝐲" %}', 'test'),
    ('{% load path2css %}{% path2css "/test/><script>alert(123)</script>" %}', 'test'),
)


@pytest.mark.parametrize("template_string,expected_output", TEMPLATES)
def test_templatetag(template_string, expected_output):
    resp = T(template_string).render(CTX).strip()
    assert resp == expected_output


@pytest.mark.xfail(condition=django.VERSION[0:2] < (1, 9),
                   reason="Django 1.8 doesn't have combination simple/assignment tags")
def test_templatetag_assignment():
    resp = T('''{% load path2css %}{% path2css "/test/" as GOOSE %}
    1{% for part in GOOSE %}---{{part}}---{% endfor %}2
    ''').render(
        CTX,
    ).strip()
    parts = [x for x in resp.split() if x]
    assert parts == ['1---test---2']
