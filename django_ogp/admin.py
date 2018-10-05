from django.contrib import admin

from django_ogp.models import BasicMeta
from django_ogp.models import ImageMate
from django_ogp.models import LocaleAlternateMeta

# Register your models here.

admin.site.register(BasicMeta)
admin.site.register(ImageMate)
admin.site.register(LocaleAlternateMeta)
