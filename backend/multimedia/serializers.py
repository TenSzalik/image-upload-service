from rest_framework.serializers import ModelSerializer

from .models import Multimedia


class MultimediaListSerializer(ModelSerializer):
    class Meta:
        model = Multimedia
        fields = [
            "id",
            "image_original",
            "image_small",
            "image_medium",
            "image_custom",
        ]
