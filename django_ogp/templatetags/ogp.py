from django import template
from django.conf import settings

from django_ogp.models import BasicMeta
from django_ogp.models import ImageMeta
from django_ogp.models import LocaleAlternateMeta

register = template.Library()


@register.inclusion_tag("django_app/ogp.html")
def show_ogp():

    data = None
    if hasattr(settings, "OGP") and settings.OGP:
        data = settings.OGP

    if not data:
        data = build_dict_db()

    return {"ogp": data}


def build_dict_db():

    metas = build_base_meta_db()

    if metas:
        metas["locales"] = build_locale_meta_db()
        metas["images"] = build_image_meta_db()

    return metas


def build_base_meta_db():
    base_meta = BasicMeta.objects.first()
    if base_meta:
        return {
            "og_title": base_meta.og_title,
            "og_type": base_meta.og_type,
            "og_description": base_meta.og_description,
            "og_url": base_meta.og_url,
            "og_site_name": base_meta.og_site_name,
            "og_determiner": _get_enum_value(base_meta.og_determiner),
        }

    else:
        return None


def _get_enum_value(value):
    values = {"1": "a", "2": "an", "3": "the", "4": "", "5": "auto"}
    return values[str(value)]


def build_image_meta_db():
    images_meta = ImageMeta.objects.all()
    metas = []
    for image in images_meta:
        metas.append(
            {
                "og_image": image.og_image,
                "og_image_url": image.og_image_url,
                "og_image_type": image.og_image_type,
                "og_image_width": image.og_image_width,
                "og_image_height": image.og_image_height,
                "og_image_alt": image.og_image_alt,
            }
        )
    return metas


def build_locale_meta_db():

    locale_metas = LocaleAlternateMeta.objects.all()
    metas = []
    for locale in locale_metas:
        metas.append({"og_locale_alternate": locale.og_locale_alternate})
    return metas
