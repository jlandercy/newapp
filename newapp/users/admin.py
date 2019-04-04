from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # https://gist.github.com/haxoza/7921eaf966a16ffb95a0
    # https://stackoverflow.com/questions/50436596/django-useradmins-add-fieldsets
    additional = [
        ('Additional Information', {
            'fields': ('tosaccepted', 'avatarcode')}
         ),
    ]

    fieldsets = tuple(list(UserAdmin.fieldsets) + additional)
    add_fieldsets = tuple(list(UserAdmin.add_fieldsets) + additional)

    list_display = ('username', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active', 'tosaccepted')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'tosaccepted')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    readonly_fields = ('last_login', 'date_joined')


# admin.site.unregister(User)
admin.site.register(CustomUser, CustomUserAdmin)
