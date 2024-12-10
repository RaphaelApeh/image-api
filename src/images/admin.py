from django.contrib import admin
from django.utils.html import format_html

from cloudinary import CloudinaryImage
from taggit.admin import TagAdmin

from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ['user__username', 'tags__name']
    readonly_fields = ['display_image', 'timestamp']

    def display_image(self, obj):
        image = obj.image
        cloudinary_image = image.build_url(width=300)
        print(image.build_url(opacity=200))
        return format_html(f'<img src="{cloudinary_image}" />')