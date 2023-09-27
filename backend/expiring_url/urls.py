from rest_framework import routers

from .views import ExpirationViewSet

router = routers.DefaultRouter()
router.register(r"expiration", ExpirationViewSet, basename="expiration")
