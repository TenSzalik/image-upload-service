from django.conf import settings
from django.db import models


class Multimedia(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="multimedia",
    )
    image_original = models.ImageField(null=True, blank=True)
    image_small = models.ImageField(null=True, blank=True)
    image_medium = models.ImageField(null=True, blank=True)
    image_custom = models.ImageField(null=True, blank=True)
