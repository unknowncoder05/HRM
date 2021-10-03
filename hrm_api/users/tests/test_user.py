# Django
from django.forms.models import model_to_dict

# Django Rest Framework
from rest_framework import status

# Models
from hrm_api.users.models import User

# Utils
from hrm_api.utils.test_utils import BaseAPITestCase
from faker import Faker
from datetime import datetime
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


class TestModelApiHelper:

    def __init__(self, client, api_base_route, model_factory, actions={}):
        self.client = client
        self.api_base_route = api_base_route
        self.model_factory = model_factory
        self.actions = actions
    
    def add_action(self, actions_name, actions_method, method_kwargs, actions_callback=None):
        self.actions[actions_name] = {
            'method' : actions_method,
            'callback' : actions_callback,
            'kwargs' : method_kwargs
        }

    def create(self, path='', **kwargs):
        instance = self.model_factory.build(**kwargs)
        data = model_to_dict(instance)
        data = {k: v for k, v in data.items() if v} # remove unset values

        request_path = f'{self.api_base_route}{path}/'
        print(f'create path: {request_path}')  # if action fails, this would help debug
        print(f'create attributes: {data}')  # if action fails, this would help debug

        return self.client.post(request_path, data, format='json'), data
    
    def force_create(self, fields={}):
        instance = self.model_factory(**fields)
        data = model_to_dict(instance)
        data = {k: v for k, v in data.items() if v}
        print(f'force_create attributes: {data}')  # if action fails, this would help debug

        return instance, data

    def retrive(self, object_id, path=''):
        request_path = f'{self.api_base_route}{path}/{object_id}/'
        print(f'retrive path: {request_path}')  # if action fails, this would help debug

        return self.client.get(request_path, format='json')
    
    def list(self, path=''):
        request_path = f'{self.api_base_route}{path}/'
        print(f'list path: {request_path}')  # if action fails, this would help debug

        return self.client.get(request_path, format='json')
    
    def update(self, object_id, fields={}, random_fields={}, path=''):
        data = fields.copy()
        request_path = f'{self.api_base_route}{path}/{object_id}/'
        print(f'update path: {request_path}')  # if action fails, this would help debug
        print(f'update attributes: {data}')  # if action fails, this would help debug

        return self.client.delete(request_path, data, format='json'), data

    def delete(self, object_id, path=''):
        request_path = f'{self.api_base_route}{path}/{object_id}/'
        print(f'delete path: {request_path}/')  # if action fails, this would help debug

        return self.client.delete(request_path, format='json')
    
    def action(self, action_name, method_kwargs={}, callback_kwargs={}):
        action = self.actions.get(action_name)
        if not action:
            raise KeyError(f'"{action_name}" is not defined as an action in this helper')
        
        response = None

        merged_method_kwargs = {**action['kwargs'], **method_kwargs}

        if action['method'] == 'create':
            response = self.create(**merged_method_kwargs)
        elif action['method'] == 'force_create':
            response = self.force_create(**merged_method_kwargs)
        elif action['method'] == 'retrive':
            response = self.retrive(**merged_method_kwargs)
        elif action['method'] == 'list':
            response = self.list(**merged_method_kwargs)
        elif action['method'] == 'update':
            response = self.update(**merged_method_kwargs)
        elif action['method'] == 'delete':
            response = self.delete(**merged_method_kwargs)

        if action['callback']:
            return action['callback'](response, **callback_kwargs)

        return response
            
# Users helper
def user_test_helper(client):
    user_model_helper = TestModelApiHelper(
        client=client,
        api_base_route='/api/v1',
        model_factory=UserFactory
    )

    def signup(res, *, force_auth=False,**kwargs):
        if force_auth:
            client.force_authenticate(user=res.id)
        return res
    
    user_model_helper.add_action(
        actions_name='signup',
        actions_method='create',
        method_kwargs={'path':'/user/sign-up'},
        actions_callback=signup
    )
    user_model_helper.add_action(
        actions_name='login',
        actions_method='create',
        method_kwargs={'path':'/auth/token'}
    )

    return user_model_helper
    
class UserTestHelper(BaseAPITestCase):
    
    api_base_route = '/api/v1'
    users_sample_data = {
        'default':{
            'first_name':'admin',
            'phone_number':'+571231231212',
            'password':'Admin123#'
        }
    }

    def signup_user(self, sample_name, *, force_auth=False):
        # Create new User with the given data
        if sample_name not in self.users_sample_data:
            raise KeyError(f'the sample "{sample_name}" is not defined')

        fake = Faker()
        data = self.users_sample_data[sample_name].copy()

        # Generate random data
        test_name = fake.name().replace(' ', '.')
        test_email = test_name+"@gmail.com"

        data['username'] = test_name
        data['email'] = test_email
        data['birth_date'] = '2021-05-05'

        request = self.user_model_helper.create(fields=data, path='/sign-up') # self.client.post(self.api_base_route + '/user/sign-up/', data, format='json')

        # If force_auth=True, force internal authentication
        if force_auth:
            self.client.force_authenticate(user=request.id)
            
        print(data)
        return request, data
    
    def login_user(self, email, password):
        data = {'email': email, 'password': password}
        request = self.client.post(self.api_base_route + '/auth/token/', data, format='json')

        print(data)
        return request, data   

    def force_create_user(self, sample_name, *, force_auth=False):
        # Create new User with the given data
        if sample_name not in self.users_sample_data:
            raise KeyError(f'the sample "{sample_name}" is not defined')

        fake = Faker()
        sample = self.users_sample_data[sample_name].copy()

        # Generate random data
        test_name = fake.name().replace(' ', '.')
        test_email = test_name+"@gmail.com"

        sample['username'] = test_name
        sample['email'] = test_email
        sample['birth_date'] = datetime.utcnow()
        user = User.objects.create(**sample)

        # If force_auth=True, force internal authentication
        if force_auth:
            self.client.force_authenticate(user=user)

        return user

class AuthApiTestCase(BaseAPITestCase):

    def setUp(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_test_helper = user_test_helper(client=self.client)
        """Test case setup."""

        # Create user
        # self.user = self.force_create_user('default', force_auth=True)
    
    # Check endpoints response status code
    def test_endpoint_responses_code(self):
        signup_request, sample = self.user_test_helper.action('signup')
        self.assertEqual(signup_request.status_code, status.HTTP_201_CREATED)

        signup_request, _ = self.user_test_helper.action('login', 
            method_kwargs = {'email':sample['email'], 'password':sample['password']}
        )
        self.assertEqual(signup_request.status_code, status.HTTP_200_OK)