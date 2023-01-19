from django.contrib import admin
from .mod_models import MOD_item
from .stat import Stat_item
from .stat_models import Action
# Register your models here.

@admin.register(MOD_item)
class MODItemAdmin(admin.ModelAdmin):
    list_display = ('message_content', 'message_ID','message_date',)
    list_filter = ['message_date',]
    search_fields = ('message_content',)


@admin.register(Stat_item)
class StatItemsAdmin(admin.ModelAdmin):
    list_display = ('stat_message', 'stat_user','stat_datetime', 'stat_ID')
    list_filter = ['stat_message','stat_datetime',]
    search_fields = ('message_content', 'stat_user',)

@admin.register(Action)
class StatItemsAdmin(admin.ModelAdmin):
    list_display = ('action', 'user','date',)
    list_filter = ['action','date',]
    search_fields = ('action', 'user',)