from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    print(UserAdmin.fieldsets)

    # https://gist.github.com/haxoza/7921eaf966a16ffb95a0
    # add_fieldsets = (
    #     ('Additional Information', {
    #         #'classes': ('wide',),
    #         'fields': ('tosaccepted',)}
    #      ),
    # )

    # list_display = ('username', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active', 'tosaccepted')
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'tosaccepted')
    # search_fields = ('username', 'first_name', 'last_name', 'email')
    # ordering = ('username',)
    # readonly_fields = ('last_login', 'date_joined', 'tosaccepted')


# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
