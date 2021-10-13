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
class ReactionFactory(DjangoModelFactory):
    class Meta:
        model = Reaction
        django_get_or_create = ('created_by', 'feed')


    feed = factory.SubFactory(FeedFactory)

    comment = factory.SubFactory(CommentFactory)

    created_by = factory.SubFactory(ProfileFactory)

    type = factory.LazyAttribute(lambda o: ReactionTypes.RANDOM)