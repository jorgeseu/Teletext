from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Annoucement, Annoucement_category

# Register your models here.

#admin.site.register(Annoucement)
#admin.site.register(Annoucement_category)


@admin.register(Annoucement)
class AnnoucementAdmin(admin.ModelAdmin):
    #permision to not change annoucement title and user by moderators
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_staff = request.user.is_staff
        disabled_fields = set()  # type:

        if is_staff:
            disabled_fields |= {
                'user',
                'title',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
    # columnt format
    search_fields = ('title',)
    list_display = ('title','category_name','annoucement_status')
    list_filter = ('annoucement_status', 'category_name',)


@admin.register(Annoucement_category)
class Annoucement_categoryAdmin(admin.ModelAdmin):
    list_filter = ['category_name']
    search_fields = ('category_name',)