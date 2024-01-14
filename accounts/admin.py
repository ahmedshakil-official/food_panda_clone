from django.contrib import admin
from accounts.models import User, UserProfile
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    list_display = ("first_name", "last_name", "email", "is_admin", "role", "is_staff", "is_active")
    ordering = ("-date_joined",)


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
