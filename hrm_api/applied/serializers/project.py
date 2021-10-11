"""Project serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from hrm_api.ideas.models import Project
from hrm_api.community.models import Feed

# Serializers
from hrm_api.utils.serializers import BasicModelSerializer



class ProjectModelSerializer(BasicModelSerializer):
    """Read Project model serializer."""

    class Meta:
        """Meta class."""

        model = Project
        fields = BasicModelSerializer.Meta.fields + (
            'id', 'name', 'description', 'question', 'feed'
        )


class CreateProjectModelSerializer(BasicModelSerializer):
    """Create Project model serializer."""

    class Meta:
        """Meta class."""

        model = Project
        fields = BasicModelSerializer.Meta.fields + (
            'name', 'description', 'question', 'feed'
        )
    
    def create(self, data): # TODO: Create feed
        """Handle created_by and feed creation."""
        users_profile = self.context['request'].user.profile
        feed = Feed.objects.create()
        user = Project.objects.create(**data, created_by=users_profile, feed=feed)
        # Send verification mail
        return user