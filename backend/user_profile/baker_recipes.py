from model_bakery import seq
from .models import AccountTier
from model_bakery.recipe import Recipe, foreign_key
from django.contrib.auth import get_user_model
from user_profile.models import AccountTier


basic_tier = Recipe(AccountTier, name="Basic")
premium_tier = Recipe(AccountTier, name="Premium")
enterprise_tier = Recipe(AccountTier, name="Enterprise")
custom_tier = Recipe(AccountTier, name="Custom")

custom_basic_user = Recipe(
    get_user_model(),
    username=seq("test_email1@example.com"),
    password=seq("foobarbaz1"),
    tier=foreign_key(basic_tier),
)

custom_premium_user = Recipe(
    get_user_model(),
    username=seq("test_email2@example.com"),
    password=seq("foobarbaz2"),
    tier=foreign_key(premium_tier),
)

custom_enterprise_user = Recipe(
    get_user_model(),
    username=seq("test_email3@example.com"),
    password=seq("foobarbaz3"),
    tier=foreign_key(enterprise_tier),
)

custom_custom_user = Recipe(
    get_user_model(),
    username=seq("test_email4@example.com"),
    password=seq("foobarbaz4"),
    tier=foreign_key(custom_tier),
)
