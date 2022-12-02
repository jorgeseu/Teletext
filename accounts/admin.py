from django.contrib import admin
from .models import UserData

from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(UserData)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserData
    list_display = ('email','name', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_active','is_superuser')
    fieldsets = (
        (None, {'fields': ('name','email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )
    search_fields = ('email','name')
    ordering = ('email',)


#admin.site.register(UserData)