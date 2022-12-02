from django.contrib import admin
from .models import Annoucement, Annoucement_category

# Register your models here.

#admin.site.register(Annoucement)
#admin.site.register(Annoucement_category)


@admin.register(Annoucement)
class AnnoucementAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_display = ('title','category_name','annoucement_status')
    list_filter = ('annoucement_status',)


@admin.register(Annoucement_category)
class Annoucement_categoryAdmin(admin.ModelAdmin):
    list_filter = ['category_name']
    search_fields = ('category_name',)