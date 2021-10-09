# Models
from hrm_api.users.models import User

# Utils
import factory
from factory.django import DjangoModelFactory

# User factory
class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        exclude = ('prefix', 'phone')

    username = factory.Faker('first_name')
    password = factory.Faker('password', length=8)

    email = factory.Faker('email')

    # phone factory
    prefix = factory.Faker('pyint', min_value=1, max_value=10**3-1)
    phone = factory.Faker('pyint', min_value=10**9, max_value=10**15-1)

    phone_number = factory.LazyAttribute(lambda p: '+{}{}'.format(p.prefix, p.phone))

    birth_date = factory.Faker('date')