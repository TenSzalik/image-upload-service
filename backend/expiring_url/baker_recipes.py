import os

from django.conf import settings
from model_bakery.recipe import Recipe

from .models import ExpirationLink


image_path = os.path.join(settings.BASE_DIR, "test_images", "example.jpg")

expiration = Recipe(ExpirationLink, available_to=300, image=image_path)
