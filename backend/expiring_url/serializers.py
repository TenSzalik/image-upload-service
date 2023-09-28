from django.db.models import Q
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.serializers import (
    ModelSerializer,
)

from .models import ExpirationLink
from multimedia.models import Multimedia


class ExpirationLinkCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpirationLink
        fields = ["available_to", "image"]

    def validate(self, data):
        if data["available_to"] > 30_000 or data["available_to"] < 300:
            raise ParseError("Expiration time is too long or too short")

        result = Multimedia.objects.filter(
            Q(image_original__exact=data["image"])
            | Q(image_small__exact=data["image"])
            | Q(image_medium__exact=data["image"])
            | Q(image_custom__exact=data["image"])
        )

        if len(result) == 0:
            raise NotFound("Multimedia not found")

        return data
