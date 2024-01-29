
from rest_framework.permissions import BasePermission
from .models import Users


class HasRolesManager(BasePermission):
    """
    Check if the user has any of the required AMP Roles
    """

    message = (
        "You do not have any Assets Management Roles, "
        "Please contact Keycloak Administrator to add roles into your Keycloak Account"
    )

    def has_permission(self, request, view):
        return request.user.is_manager

