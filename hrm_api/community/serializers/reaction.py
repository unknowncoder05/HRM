"""Reaction serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from hrm_api.community.models import Reaction


class FeedReactionModelSerializer(serializers.ModelSerializer):
    """Reaction Link model serializer."""

    class Meta:
        """Meta class."""

        model = Reaction
        fields = (
            'id', 'type', 'feed'
        )


class CommentReactionModelSerializer(serializers.ModelSerializer):
    """Read Reaction model serializer."""

    class Meta:
        """Meta class."""

        model = Reaction
        fields = (
            'id', 'type', 'comment'
        )


class CreateFeedReactionModelSerializer(serializers.ModelSerializer):
    """Create Reaction model serializer."""

    class Meta:
        """Meta class."""

        model = Reaction
        fields = (
            'id', 'type', 'feed'
        )
    
    def create(self, data):
        """Handle user and profile creation."""
        profile = self.context['request'].user.profile
        user = Reaction.objects.create(**data, created_by=profile)
        # Send verification mail
        return user


class CreateFeedReactionModelSerializer(serializers.ModelSerializer):
    """Create Reaction model serializer."""

    class Meta:
        """Meta class."""

        model = Reaction
        fields = (
            'id', 'type', 'comment'
        )
    
    def create(self, data):
        """Handle user and profile creation."""
        profile = self.context['request'].user.profile
        user = Reaction.objects.create(**data, created_by=profile)
        # Send verification mail
        return user