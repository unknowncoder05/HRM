from django.core.management.base import BaseCommand

# Factories
from hrm_api.users.factories.generators import user_generator
from hrm_api.ideas.factories.generators import idea_generator

# Utilites
import factory.random
from random import seed, randrange, random


class Command(BaseCommand):
    help = 'Generates random data for api manual testing'

    def handle(self, *args, **options):
        populate_database()


def populate_database():
    seed(1)
    factory.random.reseed_random('random_data')
    print('creating users')
    users = user_generator(10)
    print('creating ideas')
    ideas = idea_generator([
        (users[i], randrange(0,10), None)
        for i in range(len(users))
    ])