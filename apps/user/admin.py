from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from apps.user.models import User


class CustomUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        "email",
        "is_superuser"

    )
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
    )


admin.site.register(User, CustomUserAdmin)
