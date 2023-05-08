from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ('login', 'is_active',
                    'is_superuser', 'is_staff', 'is_cynologist', 'city', 'last_login')
    list_display_links = ('login',)
    fieldsets = (
        (('Персональная информация'), {'fields': ('login', 'city')}),
        (('Статус'), {
            'fields': ('is_staff', 'is_superuser', 'is_cynologist', 'is_active'),
        }),
    )

    list_filter = ()
    filter_horizontal = ()
    ordering = ()
    add_fieldsets = ()
    search_fields = ()


admin.site.register(User, UserAdmin)
