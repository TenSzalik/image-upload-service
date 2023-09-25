import pytest
from django.contrib.auth import get_user_model


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_superuser():
    admin_user = get_user_model().objects.create_superuser(
        username="super@user.com", password="foobarbaz"
    )
    assert admin_user.username == "super@user.com"
    assert admin_user.is_active is True
    assert admin_user.is_staff is True
    assert admin_user.is_superuser is True


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_superuser_without_superuser_flag():
    with pytest.raises(ValueError):
        get_user_model().objects.create_superuser(
            username="super@user.com", password="foobarbaz", is_superuser=False
        )


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_user(basic_tier):
    normal_user = get_user_model().objects.create_user(
        username="normal@user.com", password="foobarbaz", tier=basic_tier
    )
    assert normal_user.username == "normal@user.com"
    assert normal_user.is_active is True
    assert normal_user.is_staff is False
    assert normal_user.is_superuser is False
    assert normal_user.tier == basic_tier


@pytest.mark.django_db(transaction=True, reset_sequences=True)
def test_create_user_without_required_fields():
    with pytest.raises(TypeError):
        get_user_model().objects.create_user()
    with pytest.raises(TypeError):
        get_user_model().objects.create_user(username="normal@user.com")
    with pytest.raises(TypeError):
        get_user_model().objects.create_user(username="", password="foobarbaz")
    with pytest.raises(TypeError):
        get_user_model().objects.create_user(
            username="normal@user.com", password="foobarbaz"
        )
