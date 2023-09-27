import os
import uuid
from datetime import timedelta

from django.db import models
from django.utils import timezone


class ExpirationLink(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    available_to = models.PositiveIntegerField()
    image = models.CharField(max_length=255)
    key = models.UUIDField(default=uuid.uuid4, editable=False)

    def is_link_valid(self):
        created_to = self.created_at + timedelta(seconds=self.available_to)
        if created_to > timezone.now():
            return True
        else:
            return False

    def get_path_to_img(self, path):
        return os.path.join(path, self.image)

    @staticmethod
    def read_image(path):
        with open(path, "rb") as image_file:
            image_data = image_file.read()
            return image_data
