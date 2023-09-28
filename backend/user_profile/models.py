from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _
from .custom_user import CustomUserManager


class AccountTier(models.Model):
    name = models.CharField(max_length=255)
    link_expiration = models.BooleanField(default=False)
    size = ArrayField(models.PositiveIntegerField(), null=True, blank=True)
    original = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    tier = models.ForeignKey(
        AccountTier, on_delete=models.PROTECT, related_name="tier", null=True
    )
    objects = CustomUserManager()

    def __str__(self):
        return self.username
