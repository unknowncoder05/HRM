"""User permissions."""

# Django REST Framework
from rest_framework.permissions import BasePermission


class IsIdeaAdmin(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return False


class IsQuestionAdmin(BasePermission):
    """Allow access only to objects owned by the requesting user."""

    def has_object_permission(self, request, view, obj):
        """Check obj and user are the same."""
        return False