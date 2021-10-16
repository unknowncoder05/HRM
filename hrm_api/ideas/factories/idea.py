# Models
from hrm_api.ideas.models import Idea

# Utils
import factory
from factory.django import DjangoModelFactory

# Factories
from hrm_api.community.factories import FeedFactory
from hrm_api.users.factories import ProfileFactory


# Factory
class IdeaFactory(DjangoModelFactory):
    class Meta:
        model = Idea
        django_get_or_create = ('name', 'description')


    name = factory.Faker('sentence', nb_words=2)

    description = factory.Faker('sentence', nb_words=25)

    feed = factory.SubFactory(FeedFactory)

    created_by = factory.SubFactory(ProfileFactory)

    original_thinker = factory.SubFactory(ProfileFactory)

    original_thinking_date = factory.Faker('date_between')

    @factory.post_generation
    def questions(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.groups.add(*extracted)