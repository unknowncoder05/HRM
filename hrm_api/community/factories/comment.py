# Models
from hrm_api.community.models import Comment

# Utils
import factory
from factory.django import DjangoModelFactory

# Factories
from hrm_api.users.factories import ProfileFactory
from hrm_api.community.factories import FeedFactory


# Factory
class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
        django_get_or_create = ('created_by', 'content')


    feed = factory.SubFactory(FeedFactory)

    created_by = factory.SubFactory(ProfileFactory)

    content = factory.Faker('sentence', nb_words=30)