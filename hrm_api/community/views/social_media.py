"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets

# Permissions
# Permissions
from rest_framework.permissions import (
    IsAuthenticated
)
from hrm_api.users.permissions import IsLinkOwner

# Serializers
from hrm_api.community.serializers import LinkModelSerializer, CreateLinkModelSerializer

# Models

from hrm_api.community.models import Link


class LinkViewSet(viewsets.ModelViewSet):
    """Link view set.

    Handle sign up, login and account verification.
    """

    queryset = Link.objects.filter(deleted_at__isnull=True)

    serializer_class = LinkModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated, IsLinkOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in [ 'list', 'update', 'partial_update' ]:
            return queryset.filter(profile=self.request.user.profile)
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateLinkModelSerializer
        return super().get_serializer_class()