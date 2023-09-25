from rest_framework.serializers import Serializer, FileField, JSONField, ModelSerializer

from .models import Multimedia


class UploadSerializer(Serializer):
    file_uploaded = FileField()
    expiration = JSONField()

    class Meta:
        fields = ["image"]


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
