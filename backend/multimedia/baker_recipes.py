from .models import Multimedia
from model_bakery.recipe import Recipe, foreign_key
from user_profile.baker_recipes import custom_basic_user


multimedia_basic = Recipe(
    Multimedia, owner=foreign_key(custom_basic_user), image_small="example.jpg"
)
