from django.db import models


class BasicMeta(models.Model):
    A = 1
    AN = 2
    THE = 3
    EMPTY = 4
    AUTO = 5
    ENUM_DETERMINER = ((A, "a"), (AN, "an"), (THE, "the"), (EMPTY, ""), (AUTO, "auto"))

    og_title = models.CharField(max_length=155, null=True, blank=True, verbose_name="og:title")
    og_description = models.CharField(max_length=300, null=True, blank=True, verbose_name="og:description")
    og_determiner = models.IntegerField(choices=ENUM_DETERMINER, default=EMPTY, verbose_name="og:determiner")
    og_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="og:type")
    og_url = models.URLField(null=True, blank=True, verbose_name="og:url")
    og_locale = models.CharField(max_length=10, null=True, blank=True, verbose_name="og:locale")
    og_site_name = models.CharField(max_length=155, null=True, blank=True, verbose_name="og:site_name")

    class Meta:
        verbose_name = "Basic Meta"
        verbose_name_plural = "Basic Metas"

    def __str__(self):
        return "%s" % (self.og_title)


class ImageMeta(models.Model):
    og_image = models.URLField(null=True, blank=True, verbose_name="og:image")
    og_image_url = models.URLField(null=True, blank=True, verbose_name="og:image:url")
    og_image_type = models.CharField(max_length=50, null=True, blank=True, verbose_name="og:image:type")
    og_image_width = models.IntegerField(null=True, blank=True, verbose_name="og:image:width")
    og_image_height = models.IntegerField(null=True, blank=True, verbose_name="og:image:height")
    og_image_alt = models.CharField(max_length=300, null=True, blank=True, verbose_name="og:image:alt")

    class Meta:
        verbose_name = "Image Meta"
        verbose_name_plural = "Images Metas"

    def __str__(self):
        return "%s" % (self.og_image)


class LocaleAlternateMeta(models.Model):
    og_locale_alternate = models.CharField(max_length=10, null=True, blank=True, verbose_name="og:locale:alternate")

    class Meta:
        verbose_name = "Locale Alternate Meta"
        verbose_name_plural = "Locale Alternate Metas"

    def __str__(self):
        return "%s" % (self.og_locale_alternate)
