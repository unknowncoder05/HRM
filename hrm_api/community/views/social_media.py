"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)

# Serializers
from hrm_api.community.serializers import LinkModelSerializer

# Models

from hrm_api.community.models import Link


class LinkViewSet(mixins.ModelView,
                  viewsets.GenericViewSet):
    """Link view set.

    Handle sign up, login and account verification.
    """

    queryset = Link.objects.all()
    serializer_class = LinkModelSerializer
    lookup_field = 'name'

    '''def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'partial_update', 'profile']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]'''