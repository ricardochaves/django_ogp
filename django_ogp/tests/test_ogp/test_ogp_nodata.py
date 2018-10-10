# -*- coding: utf-8 -*-

from django_ogp.tests import settings
from django.test import TestCase

from django_ogp.models import BasicMeta
from django_ogp.models import ImageMeta
from django_ogp.models import LocaleAlternateMeta
from django_ogp.templatetags.ogp import show_ogp
from django.template import Context, Template

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestOGP(TestCase):

    maxDiff = None

    @patch("django_ogp.templatetags.ogp.settings.OGP", None)
    def test_show_ogp_return_none(self):
        self.assertIsNone(show_ogp()["ogp"])

    @patch("django_ogp.templatetags.ogp.settings.OGP", None)
    def test_empty_template(self):

        context = Context(show_ogp())
        template_to_render = Template("{% load ogp %}" "{% show_ogp %}")
        rendered_template = template_to_render.render(context)

        self.assertEqual(rendered_template, "")
