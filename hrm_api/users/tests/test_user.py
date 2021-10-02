# Django Rest Framework
from rest_framework import status

# Models
from hrm_api.users.models import User

# Utils
from hrm_api.utils.test_utils import BaseAPITestCase
from faker import Faker
from datetime import datetime

# Users helper
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

        request = self.client.post(self.api_base_route + '/user/sign-up/', data, format='json')

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

class AuthApiTestCase(UserTestHelper):

    def setUp(self):
        """Test case setup."""
        # Create user
        self.user = self.force_create_user('default', force_auth=True)
    
    # Check endpoints response status code
    def test_endpoint_responses_code(self):
        signup_request, sample = self.signup_user('default')
        self.assertEqual(signup_request.status_code, status.HTTP_201_CREATED)

        signup_request, _ = self.login_user(sample['email'], sample['password'])
        self.assertEqual(signup_request.status_code, status.HTTP_200_OK)