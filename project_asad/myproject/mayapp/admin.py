from django.contrib import admin

from .models import Main


admin.site.register(Main)
admin.site.site_header = 'Hello World'