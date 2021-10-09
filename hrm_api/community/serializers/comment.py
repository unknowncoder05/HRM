"""Comment serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from hrm_api.community.models import Comment


class CommentModelSerializer(serializers.ModelSerializer):
    """Read Comment model serializer."""

    class Meta:
        """Meta class."""

        model = Comment
        fields = (
            'id', 'feed', 'parent', 'created_by', 'content'
        )
    

class CreateFeedReactionModelSerializer(serializers.ModelSerializer):
    """Create Reaction model serializer."""

    class Meta:
        """Meta class."""

        model = Comment
        fields = (
            'id', 'feed', 'parent', 'content'
        )
    
    def create(self, data):
        """Handle user and profile creation."""
        profile = self.context['request'].user.profile
        user = Comment.objects.create(**data, created_by=profile)
        # Send verification mail
        return user

