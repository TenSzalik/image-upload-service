from datetime import timedelta
import uuid

from django.utils import timezone, dateformat
from freezegun import freeze_time

import pytest
from rest_framework import status


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_expiration_link(
    auth_client_enterprise, change_media_root, get_image_path, multimedia_basic
):
    image = get_image_path.split("/")[-1]
    data = {"available_to": 300, "image": image}
    response = auth_client_enterprise.post("/api/expiration/", data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert type(response.data) == uuid.UUID


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_expiration_link_image_doesnt_exist(auth_client_enterprise):
    data = {"available_to": 300, "image": "non-existent-image"}

    response = auth_client_enterprise.post("/api/expiration/", data, format="json")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_expiration_link_too_low_expiration_time(
    auth_client_enterprise, change_media_root, get_image_path
):
    image = get_image_path.split("/")[-1]
    data = {"available_to": 299, "image": image}

    response = auth_client_enterprise.post("/api/expiration/", data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_expiration_link_too_high_expiration_time(
    auth_client_enterprise, change_media_root, get_image_path
):
    image = get_image_path.split("/")[-1]
    data = {"available_to": 30_001, "image": image}
    response = auth_client_enterprise.post("/api/expiration/", data, format="json")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_read_expiration_link(auth_client_enterprise, expiration_link, read_image):
    response = auth_client_enterprise.get(f"/api/expiration/{expiration_link.key}/")

    assert response.status_code == status.HTTP_200_OK
    assert response.getvalue() == read_image


TIMEZONE_NOW_PLUS_400_SEC = dateformat.format(
    timezone.now() + timedelta(seconds=400), "Y-m-d H:i:s"
)


@freeze_time(TIMEZONE_NOW_PLUS_400_SEC)
@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_read_expiration_link_expired(
    auth_client_enterprise, expiration_link, read_image
):
    response = auth_client_enterprise.get(f"/api/expiration/{expiration_link.key}/")

    assert response.status_code == status.HTTP_410_GONE
