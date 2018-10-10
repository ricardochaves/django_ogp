from django.test import TestCase

from django_ogp.models import BasicMeta
from django_ogp.models import ImageMeta
from django_ogp.models import LocaleAlternateMeta


class TestModels(TestCase):
    def test_basic_meta(self):
        basic_meta = BasicMeta.objects.create(
            og_title="mock_og_tile",
            og_description="mock_og_description",
            og_determiner=4,
            og_type="mock_og_type",
            og_url="mock_og_url",
            og_locale="alt",
            og_site_name="mock_og_site_name",
        )

        self.assertEqual(str(basic_meta), "mock_og_tile")

    def test_image_meta(self):
        image_meta = ImageMeta.objects.create(
            og_image="mock_og_image1",
            og_image_url="mock_og_url1",
            og_image_type="mock_og_image_type1",
            og_image_width=100,
            og_image_height=200,
            og_image_alt="mock_og_image_alt1",
        )

        self.assertEqual(str(image_meta), "mock_og_image1")

    def test_locale_alternate_meta(self):
        local_meta = LocaleAlternateMeta.objects.create(og_locale_alternate="alt1")

        self.assertEqual(str(local_meta), "alt1")
