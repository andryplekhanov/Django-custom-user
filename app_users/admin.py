from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from app_users.models import ProxyGroups


class CustomUserAdmin(UserAdmin):
    ordering = ['id', ]
    list_display = ('id', 'email', 'email_confirmed', 'last_name', 'first_name', 'phone_number', 'date_joined')
    list_filter = ('date_joined', 'is_staff', 'is_active', 'email_confirmed',)
    search_fields = ('id', 'email', 'last_name', 'first_name', 'patronymic', 'phone_number')
    readonly_fields = ['date_joined', ]
    save_on_top = True
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
    make_active.short_description = _('make active')

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
    make_inactive.short_description = _('make inactive')

    fieldsets = (
        (None, {'fields': ('email', 'email_confirmed', 'password')}),
        ('Info', {'fields': ('first_name', 'last_name', 'patronymic', 'phone_number', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        ("User Details", {'fields': ('email', 'password1', 'password2')}),
        ("Permission", {'fields': ('is_active', 'is_staff', 'is_admin')}),
    )


admin.site.unregister(Group)
admin.site.register(ProxyGroups)
admin.site.register(get_user_model(), CustomUserAdmin)
