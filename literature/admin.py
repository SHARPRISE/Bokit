from django.contrib import admin
from .models import Literature
# Register your models here.

class LiteratureAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'era', 'date_posted']
    list_filter = ['date_posted']
    search_fields = ['title', 'author', 'era']
    date_hierarchy = 'date_posted'
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Literature, LiteratureAdmin)
