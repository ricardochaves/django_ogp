# Generated by Django 2.1.1 on 2018-10-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BasicMeta",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("og_title", models.CharField(blank=True, max_length=155, null=True, verbose_name="og:title")),
                (
                    "og_description",
                    models.CharField(blank=True, max_length=300, null=True, verbose_name="og:description"),
                ),
                (
                    "og_determiner",
                    models.IntegerField(
                        choices=[(1, "a"), (2, "an"), (3, "the"), (4, ""), (5, "auto")],
                        default=4,
                        verbose_name="og:determiner",
                    ),
                ),
                ("og_type", models.CharField(blank=True, max_length=50, null=True, verbose_name="og:type")),
                ("og_url", models.URLField(blank=True, null=True, verbose_name="og:url")),
                ("og_locale", models.CharField(blank=True, max_length=10, null=True, verbose_name="og:locale")),
                ("og_site_name", models.CharField(blank=True, max_length=155, null=True, verbose_name="og:site_name")),
            ],
            options={"verbose_name": "Basic Meta", "verbose_name_plural": "Basic Metas"},
        ),
        migrations.CreateModel(
            name="ImageMeta",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("og_image", models.URLField(blank=True, null=True, verbose_name="og:image")),
                ("og_image_url", models.URLField(blank=True, null=True, verbose_name="og:image:url")),
                ("og_image_type", models.CharField(blank=True, max_length=50, null=True, verbose_name="og:image:type")),
                ("og_image_width", models.IntegerField(blank=True, null=True, verbose_name="og:image:width")),
                ("og_image_height", models.IntegerField(blank=True, null=True, verbose_name="og:image:height")),
                ("og_image_alt", models.CharField(blank=True, max_length=300, null=True, verbose_name="og:image:alt")),
            ],
            options={"verbose_name": "Image Meta", "verbose_name_plural": "Images Metas"},
        ),
        migrations.CreateModel(
            name="LocaleAlternateMeta",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "og_locale_alternate",
                    models.CharField(blank=True, max_length=10, null=True, verbose_name="og:locale:alternate"),
                ),
            ],
            options={"verbose_name": "Locale Alternate Meta", "verbose_name_plural": "Locale Alternate Metas"},
        ),
    ]
