from django.contrib import admin
from academia.models import Photos

class listPhotos(admin.ModelAdmin):
    list_display = ("id", "name", "legend", "photo", "category", "visible")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    list_filter = ("category",)
    list_editable = ("visible",)


admin.site.register(Photos, listPhotos)
