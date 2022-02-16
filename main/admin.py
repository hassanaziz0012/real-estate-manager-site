from main.models import Listing, ListingImage
from django.contrib import admin

# Register your models here.
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('address', 'zip_code', 'city', 'price')
    list_filter = ('city', 'price')
    search_fields = ('address', 'city', 'zip_code')


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ('listing', 'image')

    def image(self, img):
        return img.file.name
