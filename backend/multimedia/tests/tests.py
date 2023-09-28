import os
from pathlib import Path

from django.core.files.uploadedfile import SimpleUploadedFile
import pytest
from PIL import Image
from rest_framework import status


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_basic_and_list(auth_client_basic, change_media_root, read_image):
    tmp_file = SimpleUploadedFile("file.jpg", read_image, content_type="image/jpg")
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
            "image_small": ["http:", "", "testserver", "images"],
            "image_medium": None,
            "image_custom": None,
        }
    ]
    response.json()[0]["image_small"] = (
        response.json()[0].get("image_small").split("/")[:4]
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_premium_and_list(auth_client_premium, change_media_root, read_image):
    tmp_file = SimpleUploadedFile("file.jpg", read_image, content_type="image/jpg")
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
            "image_original": ["http:", "", "testserver", "images"],
            "image_small": ["http:", "", "testserver", "images"],
            "image_medium": ["http:", "", "testserver", "images"],
            "image_custom": None,
        }
    ]
    response.json()[0]["image_original"] = (
        response.json()[0].get("image_original").split("/")[:4]
    )
    response.json()[0]["image_small"] = (
        response.json()[0].get("image_small").split("/")[:4]
    )
    response.json()[0]["image_medium"] = (
        response.json()[0].get("image_medium").split("/")[:4]
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_enterprise_and_list(
    auth_client_enterprise, change_media_root, read_image
):
    tmp_file = SimpleUploadedFile("file.jpg", read_image, content_type="image/jpg")
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
            "image_original": ["http:", "", "testserver", "images"],
            "image_small": ["http:", "", "testserver", "images"],
            "image_medium": ["http:", "", "testserver", "images"],
            "image_custom": None,
        }
    ]
    response.json()[0]["image_original"] = (
        response.json()[0].get("image_original").split("/")[:4]
    )
    response.json()[0]["image_small"] = (
        response.json()[0].get("image_small").split("/")[:4]
    )
    response.json()[0]["image_medium"] = (
        response.json()[0].get("image_medium").split("/")[:4]
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_enterprise_and_list_png(
    auth_client_enterprise, change_media_root, read_image_png
):
    tmp_file = SimpleUploadedFile("file.jpg", read_image_png, content_type="image/jpg")
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
            "image_original": ["http:", "", "testserver", "images"],
            "image_small": ["http:", "", "testserver", "images"],
            "image_medium": ["http:", "", "testserver", "images"],
            "image_custom": None,
        }
    ]
    response.json()[0]["image_original"] = (
        response.json()[0].get("image_original").split("/")[:4]
    )
    response.json()[0]["image_small"] = (
        response.json()[0].get("image_small").split("/")[:4]
    )
    response.json()[0]["image_medium"] = (
        response.json()[0].get("image_medium").split("/")[:4]
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_custom_and_list(auth_client_custom, change_media_root, read_image):
    tmp_file = SimpleUploadedFile("file.jpg", read_image, content_type="image/jpg")
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
            "image_original": ["http:", "", "testserver", "images"],
            "image_small": None,
            "image_medium": None,
            "image_custom": ["http:", "", "testserver", "images"],
        }
    ]
    response.json()[0]["image_original"] = (
        response.json()[0].get("image_original").split("/")[:4]
    )
    response.json()[0]["image_custom"] = (
        response.json()[0].get("image_custom").split("/")[:4]
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_data


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_basic_and_list_unauthorized(
    not_auth_client, change_media_root, read_image
):
    tmp_file = SimpleUploadedFile("file.jpg", read_image, content_type="image/jpg")
    response = not_auth_client.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = not_auth_client.get("/api/upload/")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_premium_do_size_is_correct(
    auth_client_basic,
    auth_client_premium,
    auth_client_enterprise,
    auth_client_custom,
    change_media_root,
    read_image,
):
    """
    Basic
    """
    tmp_file = SimpleUploadedFile("file.jpg", read_image, content_type="image/jpg")
    response = auth_client_basic.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    img_small_name = response.data["image_small"].split("/")[-1]
    img_small_path = os.path.join(change_media_root, img_small_name)
    with open(img_small_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (340, 200)

    """
    Premium
    """
    tmp_file = SimpleUploadedFile("file2.jpg", read_image, content_type="image/jpg")
    response = auth_client_premium.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    img_small_name = response.data["image_small"].split("/")[-1]
    img_small_path = os.path.join(change_media_root, img_small_name)
    with open(img_small_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (340, 200)

    img_medium_name = response.data["image_medium"].split("/")[-1]
    img_medium_path = os.path.join(change_media_root, img_medium_name)
    with open(img_medium_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (681, 400)

    img_original_name = response.data["image_original"].split("/")[-1]
    img_original_path = os.path.join(change_media_root, img_original_name)
    with open(img_original_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (1920, 1127)

    """
    Enterprise
    """
    tmp_file = SimpleUploadedFile("file3.jpg", read_image, content_type="image/jpg")
    response = auth_client_enterprise.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    img_small_name = response.data["image_small"].split("/")[-1]
    img_small_path = os.path.join(change_media_root, img_small_name)
    with open(img_small_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (340, 200)

    img_medium_name = response.data["image_medium"].split("/")[-1]
    img_medium_path = os.path.join(change_media_root, img_medium_name)
    with open(img_medium_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (681, 400)

    img_original_name = response.data["image_original"].split("/")[-1]
    img_original_path = os.path.join(change_media_root, img_original_name)
    with open(img_original_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (1920, 1127)

    """
    Custom
    """
    tmp_file = SimpleUploadedFile("file4.jpg", read_image, content_type="image/jpg")
    response = auth_client_custom.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )

    img_small_name = response.data["image_custom"].split("/")[-1]
    img_small_path = os.path.join(change_media_root, img_small_name)
    with open(img_small_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (511, 300)

    img_original_name = response.data["image_original"].split("/")[-1]
    img_original_path = os.path.join(change_media_root, img_original_name)
    with open(img_original_path, "rb") as img:
        img = Image.open(img)
        assert img.size == (1920, 1127)


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_upload_premium_do_size_is_correct_too_small_image(
    auth_client_premium, change_media_root, read_image_too_small
):
    tmp_file = SimpleUploadedFile(
        "file.png", read_image_too_small, content_type="image/png"
    )
    response = auth_client_premium.post(
        "/api/upload/", {"image": tmp_file}, format="multipart"
    )
    response.status_code == 400
