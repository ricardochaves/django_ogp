# django_ogp

[![Build Status](https://travis-ci.org/ricardochaves/django_ogp.svg?branch=master)](https://travis-ci.org/ricardochaves/django_ogp) [![Coverage Status](https://coveralls.io/repos/github/ricardochaves/django_ogp/badge.svg?branch=fix-travis)](https://coveralls.io/github/ricardochaves/django_ogp?branch=fix-travis) [![Maintainability](https://api.codeclimate.com/v1/badges/a2af8f7a30ad3bee2cac/maintainability)](https://codeclimate.com/github/ricardochaves/django_ogp/maintainability) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/3a1363cd34274377942b34418ed2b00a)](https://app.codacy.com/app/ricardochaves/django_ogp?utm_source=github.com&utm_medium=referral&utm_content=ricardochaves/django_ogp&utm_campaign=Badge_Grade_Dashboard)
 [![Updates](https://pyup.io/repos/github/ricardochaves/django_ogp/shield.svg)](https://pyup.io/repos/github/ricardochaves/django_ogp/) [![Python 3](https://pyup.io/repos/github/ricardochaves/django_ogp/python-3-shield.svg)](https://pyup.io/repos/github/ricardochaves/django_ogp/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

A more dynamic way to register Open Graph protocol

## Why

This app is made to facilitate the SEO of *"*OnePage* sites. With it you will have an administrative ready to register the metas or if you prefer to include a dictionary in your `settings.py` with the values that must be loaded.

If there is a dictionary in the settings it will not use the database and you can hide the users' [OPG](http://ogp.me/) registration by the access level of the user/group.

Now you can create [OGPs](http://ogp.me/) in an easy way.

## Suported

The test matrix guarantees coverage for:

 - pythos2·7 : Django 1.8
 - pythos2·7 : Django 1.11
 - pythos3·4 : Django 1.8
 - pythos3·4 : Django 1.9
 - pythos3·4 : Django 1.11
 - pythos3·5 : Django 1.8
 - pythos3·5 : Django 1.9
 - pythos3·5 : Django 1.11
 - pythos3·5 : Django 2.0
 - pythos3·5 : Django 2.1
 - pythos3·6 : Django 1.8
 - pythos3·6 : Django 1.9
 - pythos3·6 : Django 1.11
 - pythos3·6 : Django 2.0
 - pythos3·6 : Django 2.1
 - pythos3·7 : Django 1.8
 - pythos3·7 : Django 1.9
 - pythos3·7 : Django 1.11
 - pythos3·7 : Django 2.0
 - pythos3·7 : Django 2.1

## Install

```bash
pip install django-opg
```

Add `django-opg` in `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "django-opg",
    ...
]
```

Execute:

```bash
python manage.py migrate
```

## Usage

### Settings

You can include the metas straight into your settings. The app currently supports the following data:

```json
OGP = {
        "og_title": "Ricardo Baltazar Chaves | Site",
        "og_type": "website",
        "og_description": "My personal site.",
        "og_url": "https://www.ricardobaltazar.com/",
        "locales": [{"og_locale_alternate": "en_US"}, {"og_locale_alternate": "pt_BR"}],
        "images": [
            {
                "og_image": "https://www.ricardobaltazar.com/static/principal/images/profilepic-new.ac1b7deb01a8.jpg",
                "og_image_url": "https://www.ricardobaltazar.com/static/principal/images/profilepic-new.ac1b7deb01a8.jpg",
                "og_image_type": "image/jpeg",
                "og_image_width": 100,
                "og_image_height": 200,
                "og_image_alt": "The Ricardo image",
            },
            {
                "og_image": "https://www.ricardobaltazar.com/media/palestra_eventos/IMG_20170811_195143268.jpg.430x360_q85_box-679%2C0%2C3479%2C2340_crop_detail.jpg",
                "og_image_url": "https://www.ricardobaltazar.com/media/palestra_eventos/IMG_20170811_195143268.jpg.430x360_q85_box-679%2C0%2C3479%2C2340_crop_detail.jpg",
                "og_image_type": "image/jpeg",
                "og_image_width": 300,
                "og_image_height": 400,
                "og_image_alt": "Ricardo Speech SEO",
            },
        ],
    }
```

### DataBase

If there is no `OGP` key in the settings, the application will fetch the data in the database.

The `BasicMeta` model is selected with `first()`, so only one record can exist to prevent data from being selected.
