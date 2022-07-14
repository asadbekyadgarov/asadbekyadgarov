from django.contrib import admin

from.models import Main, MainId


class MainStyle(admin.ModelAdmin):
    list_display = ('age', 'name', 'id')
    search_fields = ('age', 'name', 'id', 'img')
    list_display_links = ('age', 'id', 'name')
    list_per_page = 5
    list_filter = ('age', 'name')



admin.site.register(Main, MainStyle)
admin.site.register(MainId)
admin.site.site_header = 'Hello World'  