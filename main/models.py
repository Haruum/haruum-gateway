from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import HaruumUserManager


class HaruumUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    password = None

    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = HaruumUserManager()

    class Meta:
        db_table = 'auth_user'

    def get_email(self):
        return self.email

