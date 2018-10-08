from django_ogp.tests import settings
from django.test import TestCase

from django_ogp.models import BasicMeta
from django_ogp.models import ImageMeta
from django_ogp.models import LocaleAlternateMeta
from django_ogp.templatetags.ogp import show_ogp

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch


# Create your tests here.
class TestOGP(TestCase):
    def setUp(self):
        BasicMeta.objects.create(
            og_title="mock_og_tile",
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

    @patch("django_ogp.templatetags.ogp.settings.OGP", None)
    def test_show_ogp_with_database(self):

        result = show_ogp()
        expected_dict = {
            "ogp": {
                "og_title": "mock_og_tile",
                "og_type": "mock_og_type",
                "og_description": "mock_og_description",
                "og_url": "mock_og_url",
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
        self.assertDictEqual(result, expected_dict)

    def test_show_ogp_with_settings(self):

        context = show_ogp()

        self.assertDictEqual(context, {"ogp": settings.OGP})
