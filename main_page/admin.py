from django.contrib import admin
from main_page.models import Main

class MainAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'date_arrival', 'age', 'weight', 'height', 'special_mark')
    search_fields = ('nickname', 'date_arrival', 'special_mark')

admin.site.register(Main, MainAdmin)

