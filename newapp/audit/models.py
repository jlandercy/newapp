import datetime

from django.db import models
from django.contrib.auth import user_logged_in, user_logged_out
from django.contrib.sessions.models import Session
from django.contrib.postgres.fields import JSONField
from django.core.serializers.json import DjangoJSONEncoder
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
        UserSession(user=user, session_id=request.session.session_key, headers=request.META).save()

    def logout_user(sender, request, user, **kwargs):
        try:
            u = UserSession.objects.get(user=user, session_id=request.session.session_key)
            u.loggedout = datetime.datetime.utcnow()
            u.save()
            # u.delete()
        except UserSession.DoesNotExist:
            pass

    user_logged_in.connect(login_user)
    user_logged_out.connect(logout_user)

    def elapsed(self):
        if self.loggedout:
            return self.loggedout - self.loggedin
        else:
            return datetime.datetime.utcnow() - self.loggedin
