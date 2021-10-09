"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets

# Permissions
# Permissions
from rest_framework.permissions import (
    IsAuthenticated
)
from hrm_api.ideas.permissions import IsProjectAdmin

# Serializers
from hrm_api.ideas.serializers import ProjectModelSerializer, CreateProjectModelSerializer

# Models

from hrm_api.ideas.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    """Project view set.

    Handle sign up, login and account verification.
    """

    queryset = Project.objects.filter(deleted_at__isnull=True)

    serializer_class = ProjectModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['update', 'partial_update']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.action in [ 'list', 'update', 'partial_update' ]:
            return queryset
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateProjectModelSerializer
        return super().get_serializer_class()