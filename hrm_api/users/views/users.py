"""Users views."""

# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from hrm_api.users.permissions import IsAccountOwner

# Serializers
from hrm_api.users.serializers.profiles import ProfileModelSerializer
from hrm_api.users.serializers import (
    UserModelSerializer,
    UserSignUpSerializer,

)

# Models
from hrm_api.users.models import User

# Utils
from hrm_api.utils.permissions import *

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """User view set.

    Handle sign up, login and account verification.
    """

    queryset = User.objects.filter(deleted_at__isnull=True, is_active=True, profile__is_public=True)
    serializer_class = UserModelSerializer
    #  lookup_field = 'username'

    def get_permissions(self):
        """Assign permissions based on action."""
        permissions = []
        if self.action in ['signup']:
            permissions += [AllowAny]
        if self.action in [*UPDATE_ACTIONS, 'profile']:
            permissions += [IsAuthenticated, IsAccountOwner]
        if not permissions:
            permissions += [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail=False, methods=['post'], url_path='sign-up')
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user = request.user
        profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data=request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)
    
    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        """Update profile data."""
        user = request.user
        data = UserModelSerializer(user).data
        return Response(data)