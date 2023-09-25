from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .custom_user import CustomUserManager


class AccountTier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tier = models.ForeignKey(
        AccountTier, on_delete=models.PROTECT, related_name="tier", null=True
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.username
