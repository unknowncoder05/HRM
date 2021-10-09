"""Project serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from hrm_api.ideas.models import Project
from hrm_api.users.models import Profile


class ProjectModelSerializer(serializers.ModelSerializer):
    """Read Project model serializer."""

    class Meta:
        """Meta class."""

        model = Project
        fields = (
            'id', 'name', 'description', 'question', 'feed'
        )


class CreateProjectModelSerializer(serializers.ModelSerializer):
    """Create Project model serializer."""

    class Meta:
        """Meta class."""

        model = Project
        fields = (
            'id', 'name', 'description', 'question', 'feed'
        )
    
    def create(self, data): # TODO: Create feed
        """Handle user and profile creation."""
        profile = self.context['request'].user.profile
        user = Project.objects.create(**data)
        # Send verification mail
        return user