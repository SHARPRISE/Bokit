from django.contrib import admin
from .models import PictureArt
# Register your models here.

class PictureArtAdmin(admin.ModelAdmin):
    list_display = ['title', 'creator', 'era', 'date_posted']
    list_filter = ['date_posted']
    search_fields = ['title', 'creator', 'era']
    date_hierarchy = 'date_posted'
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(PictureArt, PictureArtAdmin)
