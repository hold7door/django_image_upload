from django.db import models

# Create your models here.
import os
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return "users/{0}/{1:%Y%m%d%H%M%S}{2}{3}".format(instance.pk, now, milliseconds, extension)

class User(AbstractUser):
    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True)
