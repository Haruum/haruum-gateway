from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class HaruumUserManager(BaseUserManager):
    def create_user(self, email, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))

        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.save()
        return user

    def create_superuser(self, email, **extra_fields):
        user = self.create_user(email, **extra_fields)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()

        return user
