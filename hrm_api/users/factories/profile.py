# Models
from hrm_api.users.models import Profile

# Utils
import factory
from factory.django import DjangoModelFactory

# Factories
from hrm_api.users.factories import UserFactory

# factory
class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile
        django_get_or_create = ('user', )
        exclude = ('prefix', 'phone')

    user = factory.SubFactory(UserFactory)

    # picture = factory.django.ImageField(color='blue')

    biography = factory.Faker('sentence', nb_words=50)

    is_public = factory.Faker('pybool')