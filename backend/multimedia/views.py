import uuid

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from .models import Multimedia
from .multimedia_manager import (
    MultimediaModelSave,
    MultimediaModelSaveData,
    ImageSave,
    ImageSaveData,
)
from .serializers import UploadSerializer, MultimediaListSerializer


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Multimedia.objects.filter(owner=request.user.id)
        serializer = MultimediaListSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        image = request.FILES.get("image")

        data = ImageSaveData(
            image=image,
            path=settings.MEDIA_ROOT,
            image_name=uuid.uuid4().__str__(),
            image_format="." + image.content_type.split("/")[-1],
        )
        image_save = ImageSave(data=data)

        multimedia_data = MultimediaModelSaveData(model=Multimedia, owner=request.user)
        multimedia = MultimediaModelSave(data=multimedia_data)
        multimedia.get_data_for_multimedia(image_save)
        multimedia_model = multimedia.save_model()

        serializer = MultimediaListSerializer(
            multimedia_model, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
