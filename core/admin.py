from django.contrib import admin
from .mod_models import MOD_item
from .stat import Stat_item
# Register your models here.

@admin.register(MOD_item)
class MODItemAdmin(admin.ModelAdmin):
    list_display = ('message_content', 'message_ID','message_date',)
    list_filter = ['message_date',]
    search_fields = ('message_content',)


admin.site.register(Stat_item)