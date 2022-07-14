from django.contrib import admin

from .models import Main, Payment, Tovar

class MainStyle(admin.ModelAdmin):
    list_display = ('tovar_nomi',)
    prepopulated_fields = {'slug': ('tovar_nomi',)}


admin.site.register(Main)
admin.site.register(Tovar,MainStyle)
admin.site.register(Payment)