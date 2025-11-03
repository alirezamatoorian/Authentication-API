from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Otp, Profile


# Register your models here.
#
#
class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email',)
    list_filter = ('is_active',)
    search_fields = ('email',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('دسترسی‌ها', {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('تاریخ‌ها', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active')}
         ),
    )
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, UserAdmin)
admin.site.register(Otp)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name']
