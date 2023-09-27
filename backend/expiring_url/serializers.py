from django.db.models import Q
from django.http import Http404
from rest_framework.serializers import (
    ModelSerializer,
    ValidationError,
)

from .models import ExpirationLink
from multimedia.models import Multimedia


class ExpirationLinkCreateSerializer(ModelSerializer):
    class Meta:
        model = ExpirationLink
        fields = ["available_to", "image"]

    def validate(self, data):
        if data["available_to"] > 30_000 or data["available_to"] < 300:
            raise ValidationError("Error bep bop :(") # do poprawy

        result = Multimedia.objects.filter(
            Q(image_original__exact=data["image"])
            | Q(image_small__exact=data["image"])
            | Q(image_medium__exact=data["image"])
            | Q(image_custom__exact=data["image"])
        )

        if len(result) == 0:
            raise Http404("Multimedia not found")

        return data
