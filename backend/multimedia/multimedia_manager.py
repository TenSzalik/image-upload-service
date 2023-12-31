import os
from dataclasses import dataclass

import PIL
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ParseError

from .models import Multimedia


@dataclass
class ImageSaveData:
    image: InMemoryUploadedFile
    path: str
    image_name: str
    image_format: str


@dataclass
class MultimediaModelSaveData:
    model: Multimedia
    owner: get_user_model()


class ImageSave:
    """
    The class responsible for saving photo(s) to folder
    """
    def __init__(self, data: ImageSaveData) -> None:
        self.data = data

    def __call__(self, height: int | None = None) -> str:
        img = Image.open(self.data.image)

        if height is None:
            name = f"{self.data.image_name}-original" + self.data.image_format
            path = os.path.join(self.data.path, name)
            img.save(fp=path)
            return name

        height_percent = height / float(img.height)
        width = int((float(img.width) * float(height_percent)))

        if (
            (img.size[0] < height)
            or (img.size[0] < width)
            or (img.size[1] < height)
            or (img.size[1] < width)
        ):
            raise ParseError("Image is too small!")

        img.thumbnail((width, height), PIL.Image.NEAREST)

        name = f"{self.data.image_name}-{height}" + self.data.image_format
        path = os.path.join(self.data.path, name)
        img.save(fp=path)
        return name


class MultimediaModelSave:
    """
    The class responsible for handling the saving to the Multimedia's model
    """
    def __init__(self, data: MultimediaModelSaveData) -> None:
        self.data = data
        self.tier_settings = {}

    def get_data_for_multimedia(self, path_to_file: ImageSave) -> None:
        sizes = sorted(self.data.owner.tier.size)

        match self.data.owner.tier.name:
            case "Basic":
                self.tier_settings = {"image_small": path_to_file(sizes[0])}
            case "Premium":
                self.tier_settings = {
                    "image_small": path_to_file(sizes[0]),
                    "image_medium": path_to_file(sizes[1]),
                    "image_original": path_to_file(None),
                }
            case "Enterprise":
                self.tier_settings = {
                    "image_small": path_to_file(sizes[0]),
                    "image_medium": path_to_file(sizes[1]),
                    "image_original": path_to_file(None),
                }
            case _:
                self.tier_settings = {
                    "image_custom": path_to_file(sizes[0]),
                    "image_original": path_to_file(None),
                }

    def save_model(self) -> Multimedia():
        multimedia = self.data.model(owner=self.data.owner, **self.tier_settings)
        multimedia.save()
        return multimedia
