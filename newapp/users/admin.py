from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active']

    print(UserAdmin.fieldsets)

    # Remove Password form Form but the error still raises
    # exclude = ('password',)

    # fieldsets = tuple(
    #     list(UserAdmin.fieldsets) +
    #     [('Additional Informations', {
    #         'fields': ('tosaccepted', 'avatarcode',),
    #     })]
    # )


admin.site.register(CustomUser, CustomUserAdmin)
