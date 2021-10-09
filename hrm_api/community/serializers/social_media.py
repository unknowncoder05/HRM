"""Link serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from hrm_api.community.models import Link
from hrm_api.users.models import Profile


class LinkModelSerializer(serializers.ModelSerializer):
    """Read Link model serializer."""

    class Meta:
        """Meta class."""

        model = Link
        fields = (
            'id', 'description', 'url'
        )


class CreateLinkModelSerializer(serializers.ModelSerializer):
    """Create Link model serializer."""

    class Meta:
        """Meta class."""

        model = Link
        fields = (
            'id', 'description', 'url'
        )
    
    def create(self, data):
        """Handle user and profile creation."""
        profile = self.context['request'].user.profile
        user = Link.objects.create(**data, profile=profile)
        # Send verification mail
        return user