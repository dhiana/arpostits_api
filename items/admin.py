from django.contrib import admin
from .models import Item
from tasks.models import Task

class TaskInline(admin.TabularInline):
    model = Task

class ItemAdmin(admin.ModelAdmin):
    inlines = [TaskInline,]
    list_display = ['title', 'project', 'marker', 'progress', 'ready', 'blocked']
    list_editable = ['marker', 'progress', 'ready', 'blocked']

admin.site.register(Item, ItemAdmin)
