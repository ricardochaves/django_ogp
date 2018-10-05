DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "mydatabase"}}

DEBUG = True

INSTALLED_APPS = ["django_ogp"]

SECRET_KEY = "dfsfds"

TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
