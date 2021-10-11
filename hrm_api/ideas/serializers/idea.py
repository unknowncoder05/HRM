"""Idea serializer."""

# Models
from hrm_api.ideas.models import Idea
from hrm_api.community.models import Feed
from hrm_api.utils.serializers import BasicModelSerializer


class IdeaModelSerializer(BasicModelSerializer):
    """Read Idea model serializer."""

    class Meta:
        """Meta class."""

        model = Idea
        fields = BasicModelSerializer.Meta.fields + (
            'description', 'feed', 'created_by', 'original_thinker', 'original_thinking_date'
        )


class CreateIdeaModelSerializer(BasicModelSerializer):
    """Create Idea model serializer."""

    class Meta:
        """Meta class."""

        model = Idea
        fields = BasicModelSerializer.Meta.fields + (
            'id', 'description', 'original_thinker', 'original_thinking_date'
        )
    
    def create(self, data): # TODO: Create feed
        """Handle created_by and feed creation."""
        users_profile = self.context['request'].user.profile
        feed = Feed.objects.create()
        user = Idea.objects.create(**data, created_by=users_profile, feed=feed)
        # Send verification mail
        return user