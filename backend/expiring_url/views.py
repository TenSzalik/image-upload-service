import os
from django.conf import settings
from django.http import HttpResponse
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import ExpirationLinkCreateSerializer
from .models import ExpirationLink
from .permissions import ExpirationCreatePermission


class ExpirationViewSet(ViewSet):
    permission_classes = (ExpirationCreatePermission,)

    def get_serializer_class(self):
        if self.action in ("create"):
            return ExpirationLinkCreateSerializer
        return super().get_serializer_class()

    def retrieve(self, request, pk):
        try:
            queryset = ExpirationLink.objects.get(key=pk)
        except IndexError:
            return Response(
                f"There is no image with name {pk}", status=status.HTTP_404_NOT_FOUND
            )

        if queryset.is_link_valid() == False:
            return Response({"detail": "Link expired"}, status=status.HTTP_410_GONE)

        path_to_img = queryset.get_path_to_img(settings.MEDIA_ROOT)
        return HttpResponse(queryset.read_image(path_to_img), content_type="image/jpeg")

    def create(self, request):
        serializer = self.get_serializer_class()
        serializer_data = serializer(data=request.data)

        if not serializer_data.is_valid():
            return Response(
                {"detail": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST
            )

        model = ExpirationLink(
            available_to=request.data.get("available_to"),
            image=request.data.get("image"),
        )
        model.save()
        expiration_link_to_img = os.path.join("/api/expiration/", model.key.__str__())
        return Response(expiration_link_to_img, status=status.HTTP_201_CREATED)
