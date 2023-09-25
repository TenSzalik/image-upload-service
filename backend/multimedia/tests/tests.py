from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
import pytest
from rest_framework import status


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_basic_and_list(auth_client_basic, change_media_root):
    p = Path(__file__).with_name("file.jpg")
    with p.open("rb") as image_file:
        image_data = image_file.read()

    tmp_file = SimpleUploadedFile("file.jpg", image_data, content_type="image/jpg")
    response = auth_client_basic.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["id"] is 1
    assert response.data["image_original"] is None
    assert response.data["image_small"] is not None
    assert response.data["image_medium"] is None
    assert response.data["image_custom"] is None

    response = auth_client_basic.get("/api/upload/")

    expected_data = [
        {
            "id": 1,
            "image_original": None,
            "image_small": ['http:', '', 'testserver', 'images'],
            "image_medium": None,
            "image_custom": None,
        }
    ]
    response.json()[0]["image_small"] = response.json()[0].get("image_small").split("/")[:4]

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_premium_and_list(auth_client_premium, change_media_root):
    p = Path(__file__).with_name("file.jpg")
    with p.open("rb") as image_file:
        image_data = image_file.read()

    tmp_file = SimpleUploadedFile("file.jpg", image_data, content_type="image/jpg")
    response = auth_client_premium.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["id"] is 1
    assert response.data["image_original"] is not None
    assert response.data["image_small"] is not None
    assert response.data["image_medium"] is not None
    assert response.data["image_custom"] is None

    response = auth_client_premium.get("/api/upload/")

    expected_data = [
        {
            "id": 1,
            "image_original": ['http:', '', 'testserver', 'images'],
            "image_small": ['http:', '', 'testserver', 'images'],
            "image_medium": ['http:', '', 'testserver', 'images'],
            "image_custom": None,
        }
    ]
    response.json()[0]["image_original"] = response.json()[0].get("image_original").split("/")[:4]
    response.json()[0]["image_small"] = response.json()[0].get("image_small").split("/")[:4]
    response.json()[0]["image_medium"] = response.json()[0].get("image_medium").split("/")[:4]
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_enterprise_and_list(auth_client_enterprise, change_media_root):
    p = Path(__file__).with_name("file.jpg")
    with p.open("rb") as image_file:
        image_data = image_file.read()

    tmp_file = SimpleUploadedFile("file.jpg", image_data, content_type="image/jpg")
    response = auth_client_enterprise.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["id"] is 1
    assert response.data["image_original"] is not None
    assert response.data["image_small"] is not None
    assert response.data["image_medium"] is not None
    assert response.data["image_custom"] is None

    response = auth_client_enterprise.get("/api/upload/")

    expected_data = [
        {
            "id": 1,
            "image_original": ['http:', '', 'testserver', 'images'],
            "image_small": ['http:', '', 'testserver', 'images'],
            "image_medium": ['http:', '', 'testserver', 'images'],
            "image_custom": None,
        }
    ]
    response.json()[0]["image_original"] = response.json()[0].get("image_original").split("/")[:4]
    response.json()[0]["image_small"] = response.json()[0].get("image_small").split("/")[:4]
    response.json()[0]["image_medium"] = response.json()[0].get("image_medium").split("/")[:4]
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_custom_and_list(auth_client_custom, change_media_root):
    p = Path(__file__).with_name("file.jpg")
    with p.open("rb") as image_file:
        image_data = image_file.read()

    tmp_file = SimpleUploadedFile("file.jpg", image_data, content_type="image/jpg")
    response = auth_client_custom.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["id"] is 1
    assert response.data["image_original"] is not None
    assert response.data["image_small"] is None
    assert response.data["image_medium"] is None
    assert response.data["image_custom"] is not None

    response = auth_client_custom.get("/api/upload/")

    expected_data = [
        {
            "id": 1,
            "image_original": ['http:', '', 'testserver', 'images'],
            "image_small": None,
            "image_medium": None,
            "image_custom": ['http:', '', 'testserver', 'images'],
        }
    ]
    response.json()[0]["image_original"] = response.json()[0].get("image_original").split("/")[:4]
    response.json()[0]["image_custom"] = response.json()[0].get("image_custom").split("/")[:4]
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_basic_and_list_unauthorized(not_auth_client, change_media_root):
    p = Path(__file__).with_name("file.jpg")
    with p.open("rb") as image_file:
        image_data = image_file.read()

    tmp_file = SimpleUploadedFile("file.jpg", image_data, content_type="image/jpg")

    response = not_auth_client.post(
            "/api/upload/", {"image": tmp_file}, format="multipart"
        )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = not_auth_client.get("/api/upload/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
