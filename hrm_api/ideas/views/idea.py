"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets

# Permissions
# Permissions
from rest_framework.permissions import (
    IsAuthenticated
)
from hrm_api.ideas.permissions import IsIdeaAdmin

# Serializers
from hrm_api.ideas.serializers import IdeaModelSerializer, CreateIdeaModelSerializer

# Models

from hrm_api.ideas.models import Idea


class IdeaViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """Idea view set.

    Handle sign up, login and account verification.
    """

    queryset = Idea.objects.filter(deleted_at__isnull=True)

    serializer_class = IdeaModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateIdeaModelSerializer
        return super().get_serializer_class()