from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# https://regex101.com/
avatarValidator = RegexValidator(r"^&#[x]{0,1}[\da-fA-f]{2,5};$", "Avatar code is a single HTML symbol like <code>&#64;</code>")

def validate_Checked(value):
    if not bool(value):
        raise ValidationError("This parameter must be checked.")

class CustomUser(AbstractUser):

    tosaccepted = models.BooleanField('TOS Accepted', default=False,
                      validators=[validate_Checked],
                      help_text='Term Of Services accepted.')
    avatarcode = models.CharField('Avatar Code', max_length=8, default='&#64;',
                      validators=[avatarValidator],
                      help_text='See <a href="https://www.toptal.com/designers/htmlarrows/symbols/">examples</a>.')

