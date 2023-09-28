import os
import tempfile

import pytest
from rest_framework.test import APIClient

from model_bakery import baker


"""
All possible types of users
"""


@pytest.fixture(name="user_basic")
def fixture_user_basic():
    return baker.make_recipe("user_profile.custom_basic_user", _quantity=2)


@pytest.fixture(name="user_premium")
def fixture_user_premium():
    return baker.make_recipe("user_profile.custom_premium_user", _quantity=2)


@pytest.fixture(name="user_enterprise")
def fixture_user_enterprise():
    return baker.make_recipe("user_profile.custom_enterprise_user", _quantity=2)


@pytest.fixture(name="user_custom")
def fixture_user_custom():
    return baker.make_recipe("user_profile.custom_custom_user", _quantity=2)


@pytest.fixture(name="user_custom_without_link_expiration_access")
def fixture_user_custom_without_link_expiration_access():
    return baker.make_recipe(
        "user_profile.custom_custom_user_without_link_expiration_access", _quantity=2
    )


"""
All possible types of authenticated users and unauthenticated
"""


@pytest.fixture(name="not_auth_client")
def fixture_not_auth_client() -> APIClient:
    client = APIClient()
    return client


@pytest.fixture(name="auth_client_basic")
def fixture_auth_client_basic(user_basic) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user_basic[0])
    return client


@pytest.fixture(name="auth_client_premium")
def fixture_auth_client_premium(user_premium) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user_premium[0])
    return client


@pytest.fixture(name="auth_client_enterprise")
def fixture_auth_client_enterprise(user_enterprise) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user_enterprise[0])
    return client


@pytest.fixture(name="auth_client_custom")
def fixture_auth_client_custom(user_custom) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user_custom[0])
    return client


@pytest.fixture(name="auth_client_custom_without_link_expiration_access")
def fixture_auth_client_custom_without_link_expiration_access(
    user_custom_without_link_expiration_access,
) -> APIClient:
    client = APIClient()
    client.force_authenticate(user=user_custom_without_link_expiration_access[0])
    return client


"""
Regular models
"""


@pytest.fixture(name="basic_tier")
def fixture_basic_tier():
    return baker.make_recipe("user_profile.basic_tier")


@pytest.fixture(name="expiration_link")
def expiration_link():
    return baker.make_recipe("expiring_url.expiration")


@pytest.fixture(name="multimedia_basic")
def multimedia_basic():
    return baker.make_recipe("multimedia.multimedia_basic")


@pytest.fixture(name="change_media_root")
def fixture_change_media_root(settings, temp_dir):
    """
    Override and return the MEDIA_ROOT path to the path of the temporary directory
    Place all created images in this directory
    """
    settings.MEDIA_ROOT = temp_dir
    return settings.MEDIA_ROOT


@pytest.fixture(scope="module", name="temp_dir")
def fixture_temp_dir():
    """
    Create temporary directory and remove it eg. '/tmp/tmpkdxh666y'
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname


@pytest.fixture(name="get_image_path")
def fixture_get_image_path(settings):
    """
    Get path to the tested image jpg
    """
    image_path = os.path.join(settings.BASE_DIR, "example.jpg")
    return image_path


@pytest.fixture(name="get_image_png_path")
def fixture_get_image_png_path(settings):
    """
    Get path to the tested image png
    """
    image_path = os.path.join(settings.BASE_DIR, "example.png")
    return image_path


@pytest.fixture(name="get_too_small_image_path")
def fixture_get_too_small_image_path(settings):
    """
    Get path to the too small tested image
    """
    image_path = os.path.join(settings.BASE_DIR, "example_too_small.png")
    return image_path


@pytest.fixture(name="read_image")
def fixture_read_image(settings, get_image_path):
    """
    Read the example image and return a string of bytes
    """
    with open(get_image_path, "rb") as image_file:
        return image_file.read()


@pytest.fixture(name="read_image_png")
def fixture_read_image_png(settings, get_image_png_path):
    """
    Read the example image and return a string of bytes
    """
    with open(get_image_png_path, "rb") as image_file:
        return image_file.read()


@pytest.fixture(name="read_image_too_small")
def fixture_read_image_too_small(settings, get_too_small_image_path):
    """
    Read the example image and return a string of bytes
    """
    with open(get_too_small_image_path, "rb") as image_file:
        return image_file.read()
