import tempfile

import pytest
from rest_framework.test import APIClient

from model_bakery import baker


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


@pytest.fixture(name="basic_tier")
def fixture_basic_tier():
    return baker.make_recipe("user_profile.basic_tier")


@pytest.fixture(name="change_media_root")
def fixture_change_media_root(settings, temp_dir):
    settings.MEDIA_ROOT = temp_dir


@pytest.fixture(scope="module", name="temp_dir")
def fixture_temp_dir():
    """
    Create temporary directory and remove it eg. '/tmp/tmpkdxh666y'
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield tmpdirname
