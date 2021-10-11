"""Question serializer."""

# Models
from hrm_api.ideas.models import Question
from hrm_api.community.models import Feed
from hrm_api.utils.serializers import BasicModelSerializer


class QuestionModelSerializer(BasicModelSerializer):
    """Read Question model serializer."""

    class Meta:
        """Meta class."""

        model = Question
        fields = BasicModelSerializer.Meta.fields + (
            'description', 'feed', 'created_by', 'original_questioner', 'original_ask_date'
        )


class CreateQuestionModelSerializer(BasicModelSerializer):
    """Create Question model serializer."""

    class Meta:
        """Meta class."""

        model = Question
        fields = BasicModelSerializer.Meta.fields + (
            'id', 'description', 'original_questioner', 'original_ask_date'
        )
    
    def create(self, data): # TODO: Create feed
        """Handle created_by and feed creation."""
        users_profile = self.context['request'].user.profile
        feed = Feed.objects.create()
        user = Question.objects.create(**data, created_by=users_profile, feed=feed)
        # Send verification mail
        return user