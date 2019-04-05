from django.contrib import admin

from .models import UserSession


# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site
@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'loggedin', 'loggedout', 'elapsed', 'is_active', 'session')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ('-id',)
    readonly_fields = ('id', 'user', 'loggedin', 'loggedout', 'session', 'is_active', 'headers')
