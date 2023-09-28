from rest_framework import permissions


class ExpirationCreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "POST":
            if request.user.username == "":
                return False
            return request.user.tier.link_expiration
        return True
