from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('id', 'last_login', 'date_joined', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'password', 'profile_picture')
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Outras informações', {
            'fields': ('last_login', 'date_joined', 'updated_at')
        })
    )