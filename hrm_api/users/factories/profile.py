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
        exclude = ('prefix', 'phone')

    username = factory.Faker('first_name')
    password = factory.Faker('password', length=8)

    email = factory.Faker('email')

    # phone factory
    prefix = factory.Faker('pyint', min_value=1, max_value=10**3-1)
    phone = factory.Faker('pyint', min_value=10**9, max_value=10**15-1)

    phone_number = factory.LazyAttribute(lambda p: '+{}{}'.format(p.prefix, p.phone))

    birth_date = factory.Faker('date')




    user = factory.SubFactory(UserFactory)

    picture = factory.django.ImageField(color='blue')

    biography = factory.Faker('paragraph', nb_sentences=50)

    is_public = factory.Faker('pybool')