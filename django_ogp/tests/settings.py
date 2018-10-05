DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "mydatabase"}}

DEBUG = True

INSTALLED_APPS = ["django_ogp"]

SECRET_KEY = "dfsfds"

OGP = {
    "og_title": "db_tile",
    "og_type": "db_type",
    "og_description": "db_description",
    "og_url": "db_url",
    "locales": [{"og_locale_alternate": "alt1"}, {"og_locale_alternate": "alt2"}],
    "images": [
        {
            "og_image": "db_image1",
            "og_image_url": "db_url1",
            "og_image_type": "db_image_type1",
            "og_image_width": 100,
            "og_image_height": 200,
            "og_image_alt": "db_image_alt1",
        },
        {
            "og_image": "db_image2",
            "og_image_url": "db_url2",
            "og_image_type": "db_image_type2",
            "og_image_width": 300,
            "og_image_height": 400,
            "og_image_alt": "db_image_alt2",
        },
    ],
}
