from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    tosaccepted = models.BooleanField('TOS Accepted', default=False)
    avatarcode = models.CharField('Avatar Code', max_length=8, default='&#64;')

