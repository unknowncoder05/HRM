# Models
from hrm_api.community.models import Reaction

# Utils
import factory
from factory.django import DjangoModelFactory
from hrm_api.community.models.reaction import ReactionTypes


# Factories
from hrm_api.users.factories import ProfileFactory
from hrm_api.community.factories import FeedFactory, CommentFactory


# Factory
class FeedReactionFactory(DjangoModelFactory):
    class Meta:
        model = Reaction
        django_get_or_create = ('created_by', 'feed')

    created_by = factory.SubFactory(ProfileFactory)

    type = factory.LazyAttribute(lambda o: ReactionTypes.RANDOM)

class CommentReactionFactory(DjangoModelFactory):
    class Meta:
        model = Reaction
        django_get_or_create = ('created_by', 'comment')

    created_by = factory.SubFactory(ProfileFactory)

    type = factory.LazyAttribute(lambda o: ReactionTypes.RANDOM)