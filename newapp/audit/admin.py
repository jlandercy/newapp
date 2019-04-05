from django.contrib import admin

from .models import UserSession


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'loggedin', 'loggedout', 'session', 'is_active')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ('-id',)
    readonly_fields = ('id', 'user', 'loggedin', 'loggedout', 'session', 'is_active', 'headers')
