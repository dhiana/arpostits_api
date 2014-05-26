from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    pass
    list_display = ['title', 'marker', 'progress', 'ready', 'blocked']
    list_editable = ['marker', 'progress', 'ready', 'blocked']

admin.site.register(Item, ItemAdmin)
