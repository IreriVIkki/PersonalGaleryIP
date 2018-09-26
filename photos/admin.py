from django.contrib import admin
from .models import Image, categories, Location


class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)


admin.site.register(Image, ImageAdmin)
admin.site.register(categories)
admin.site.register(Location)
