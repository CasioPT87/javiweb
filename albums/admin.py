from django.contrib import admin

# Register your models here.

from .models import Album, Photo, PhotoCarrousel

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(PhotoCarrousel)
