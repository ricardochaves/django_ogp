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

    def setUp(self):
        BasicMeta.objects.create(
            og_title="mock_og_title",
            og_description="mock_og_description",
            og_determiner=4,
            og_type="mock_og_type",
            og_url="mock_og_url",
            og_locale="alt",
            og_site_name="mock_og_site_name",
        )

        ImageMeta.objects.create(
            og_image="mock_og_image1",
            og_image_url="mock_og_url1",
            og_image_type="mock_og_image_type1",
            og_image_width=100,
            og_image_height=200,
            og_image_alt="mock_og_image_alt1",
        )
        ImageMeta.objects.create(
            og_image="mock_og_image2",
            og_image_url="mock_og_url2",
            og_image_type="mock_og_image_type2",
            og_image_width=300,
            og_image_height=400,
            og_image_alt="mock_og_image_alt2",
        )

        LocaleAlternateMeta.objects.create(og_locale_alternate="alt1")
        LocaleAlternateMeta.objects.create(og_locale_alternate="alt2")

        context = Context(show_ogp())
        template_to_render = Template("{% load ogp %}" "{% show_ogp %}")
        self.rendered_template = template_to_render.render(context)

    @patch("django_ogp.templatetags.ogp.settings.OGP", None)
    def test_show_ogp_with_database(self):

        result = show_ogp()

        expected_dict_3 = {
            "ogp": {
                "og_title": "mock_og_title",
                "og_type": "mock_og_type",
                "og_description": "mock_og_description",
                "og_url": "mock_og_url",
                "og_site_name": "mock_og_site_name",
                "og_determiner": "",
                "locales": [{"og_locale_alternate": "alt1"}, {"og_locale_alternate": "alt2"}],
                "images": [
                    {
                        "og_image": "mock_og_image1",
                        "og_image_url": "mock_og_url1",
                        "og_image_type": "mock_og_image_type1",
                        "og_image_width": 100,
                        "og_image_height": 200,
                        "og_image_alt": "mock_og_image_alt1",
                    },
                    {
                        "og_image": "mock_og_image2",
                        "og_image_url": "mock_og_url2",
                        "og_image_type": "mock_og_image_type2",
                        "og_image_width": 300,
                        "og_image_height": 400,
                        "og_image_alt": "mock_og_image_alt2",
                    },
                ],
            }
        }

        expected_dict_2 = {
            "ogp": {
                "og_title": u"mock_og_title",
                "og_type": u"mock_og_type",
                "og_description": u"mock_og_description",
                "og_url": u"mock_og_url",
                "og_site_name": u"mock_og_site_name",
                "og_determiner": u"",
                "locales": [{"og_locale_alternate": u"alt1"}, {"og_locale_alternate": u"alt2"}],
                "images": [
                    {
                        "og_image": u"mock_og_image1",
                        "og_image_url": u"mock_og_url1",
                        "og_image_type": u"mock_og_image_type1",
                        "og_image_width": 100,
                        "og_image_height": 200,
                        "og_image_alt": u"mock_og_image_alt1",
                    },
                    {
                        "og_image": u"mock_og_image2",
                        "og_image_url": u"mock_og_url2",
                        "og_image_type": u"mock_og_image_type2",
                        "og_image_width": 300,
                        "og_image_height": 400,
                        "og_image_alt": u"mock_og_image_alt2",
                    },
                ],
            }
        }

        if result["ogp"]["og_title"] == u"mock_og_title":
            self.assertDictEqual(result, expected_dict_2)
        else:
            self.assertDictEqual(result, expected_dict_3)

    def test_show_ogp_with_settings(self):

        context = show_ogp()

        self.assertDictEqual(context, {"ogp": settings.OGP})

    def test_url_template(self):
        self.assertInHTML('<meta property="og:url" content="db_url">', self.rendered_template)

    def test_title_template(self):
        self.assertInHTML('<meta property="og:title" content="db_title">', self.rendered_template)

    def test_site_name_template(self):
        self.assertInHTML('<meta property="og:site_name" content="db_site_name">', self.rendered_template)

    def test_description_template(self):
        self.assertInHTML('<meta property="og:description" content="db_description">', self.rendered_template)

    def test_determiner_template(self):
        self.assertInHTML('<meta property="og:determiner" content="">', self.rendered_template)

    def test_type_template(self):
        self.assertInHTML('<meta property="og:type" content="db_type">', self.rendered_template)

    def test_locale_template(self):
        self.assertInHTML('<meta property="og:locale" content="en-US">', self.rendered_template)

    def test_locale_alternate1_template(self):
        self.assertInHTML('<meta property="og:locale:alternate" content="alt1" />', self.rendered_template)

    def test_locale_alternate2_template(self):
        self.assertInHTML('<meta property="og:locale:alternate" content="alt2" />', self.rendered_template)

    def test_og_image1_template(self):
        self.assertInHTML('<meta property="og:image" content="db_image1" />', self.rendered_template)

    def test_secure_url1_template(self):
        self.assertInHTML('<meta property="og:image:secure_url" content="db_url1" />', self.rendered_template)

    def test_secure_type1_template(self):
        self.assertInHTML('<meta property="og:image:type" content="db_image_type1" />', self.rendered_template)

    def test_width1_template(self):
        self.assertInHTML('<meta property="og:image:width" content="100" />', self.rendered_template)

    def test_height1_template(self):
        self.assertInHTML('<meta property="og:image:height" content="200" />', self.rendered_template)

    def test_image_alt1_template(self):
        self.assertInHTML('<meta property="og:image:alt" content="db_image_alt1" />', self.rendered_template)

    def test_og_image2_template(self):
        self.assertInHTML('<meta property="og:image" content="db_image2" />', self.rendered_template)

    def test_secure_url2_template(self):
        self.assertInHTML('<meta property="og:image:secure_url" content="db_url2" />', self.rendered_template)

    def test_secure_type2_template(self):
        self.assertInHTML('<meta property="og:image:type" content="db_image_type2" />', self.rendered_template)

    def test_width2_template(self):
        self.assertInHTML('<meta property="og:image:width" content="300" />', self.rendered_template)

    def test_height2_template(self):
        self.assertInHTML('<meta property="og:image:height" content="400" />', self.rendered_template)

    def test_image_alt2_template(self):
        self.assertInHTML('<meta property="og:image:alt" content="db_image_alt2" />', self.rendered_template)
