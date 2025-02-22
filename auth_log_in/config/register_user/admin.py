from django.contrib import admin
from django.apps import apps
'''
app_models = apps.get_app_config('register_user').get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
'''

from django.contrib import admin
from .models import CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'gender','role', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    list_filter = ('is_active', 'gender')
    ordering = ('-date_joined',)


    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'phone_number', 'age', 'gender')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
    )