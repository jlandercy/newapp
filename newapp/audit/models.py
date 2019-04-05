import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import user_logged_in, user_logged_out
from django.contrib.sessions.models import Session
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

from users.models import CustomUser


class SafeEncoder(DjangoJSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except:
            return str(obj)


class UserSession(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.SET_NULL, null=True)
    loggedin = models.DateTimeField(auto_now_add=True)
    loggedout = models.DateTimeField(default=None, null=True)
    headers = JSONField(encoder=SafeEncoder, default=dict)

    def __str__(self):
        return self.user.username

    def login_user(sender, request, user, **kwargs):
        """Log User Session creation"""
        UserSession(user=user, session_id=request.session.session_key, headers=request.META).save()

    def logout_user(sender, request, user, **kwargs):
        """Log User Session destruction"""
        try:
            u = UserSession.objects.get(user=user, session_id=request.session.session_key)
            u.loggedout = timezone.now()
            u.save()
            # u.delete()
        except UserSession.DoesNotExist:
            pass

    # Event binding:
    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)

    def elapsed(self):
        """Elapsed time since logged in"""
        if self.loggedout:
            return self.loggedout - self.loggedin
        else:
            return timezone.now() - self.loggedin

    def is_active(self):
        """Is the session active"""
        return (self.loggedout is None) or not(self.session_id is None)
