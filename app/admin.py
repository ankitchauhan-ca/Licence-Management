# licenses/admin.py

from django.contrib import admin
from .models import License

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('key', 'user_email', 'expiration_date', 'is_revoked')
    list_filter = ('is_revoked',)
    search_fields = ('key', 'user_email')

admin.site.register(License, LicenseAdmin)
