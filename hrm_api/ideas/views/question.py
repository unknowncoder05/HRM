"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets

# Permissions
# Permissions
from rest_framework.permissions import (
    IsAuthenticated
)
from hrm_api.ideas.permissions import IsQuestionAdmin

# Serializers
from hrm_api.ideas.serializers import QuestionModelSerializer, CreateQuestionModelSerializer

# Models

from hrm_api.ideas.models import Question


class QuestionViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """Question view set.

    Handle sign up, login and account verification.
    """

    queryset = Question.objects.filter(deleted_at__isnull=True)

    serializer_class = QuestionModelSerializer

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
            return CreateQuestionModelSerializer
        return super().get_serializer_class()