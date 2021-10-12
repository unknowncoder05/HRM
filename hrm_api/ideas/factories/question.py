# Models
from hrm_api.ideas.models import Question

# Utils
import factory
from factory.django import DjangoModelFactory

# Factories
from hrm_api.ideas.factories import IdeasFactory
from hrm_api.community.factories import FeedFactory
from hrm_api.users.factories import ProfileFactory


# Factory
class QuestionFactory(DjangoModelFactory):
    class Meta:
        model = Question
        django_get_or_create = ('description', )

    description = factory.Faker('paragraph', nb_sentences=10)

    feed = factory.SubFactory(FeedFactory)

    created_by = factory.SubFactory(ProfileFactory)

    original_questioner = factory.SubFactory(ProfileFactory)

    original_ask_date = factory.Faker('date_between')

    @factory.post_generation
    def ideas(self, create, extracted, **kwargs):
        if not create or not extracted:
            # Simple build, or nothing to add, do nothing.
            return

        # Add the iterable of groups using bulk addition
        self.groups.add(*extracted)