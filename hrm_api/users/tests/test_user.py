# Django Rest Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Models
from hrm_api.users.models import User

# Utils
from hrm_api.users.helpers import user_test_helper


class AuthApiTestCase(APITestCase):

    def setUp(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_test_helper = user_test_helper(client=self.client)
        """Test case setup."""

        # Create user
        # self.user = self.force_create_user('default', force_auth=True)
    
    # Check endpoints response status code
    def test_sign_up_and_log_in(self): # TODO: check if created in DB
        signup_request, sample = self.user_test_helper.action('signup')
        self.assertEqual(signup_request.status_code, status.HTTP_201_CREATED)

        login_request, _ = self.user_test_helper.action('login', 
            method_kwargs = {'email':sample['email'], 'password':sample['password']}
        )
        self.assertEqual(login_request.status_code, status.HTTP_200_OK)
    
    def test_profile_patch(self): # TODO: check attributes
        signup_request, sample = self.user_test_helper.action('signup')
        user = User.objects.get(id=signup_request.json()['id'])
        self.client.force_authenticate(user=user)

        change_user_data={'biography':'changed biography', 'is_public':False}

        login_request, _ = self.user_test_helper.action('patch_profile', 
            method_kwargs = {'object_id': None, 'fields':change_user_data}
        )
        self.assertEqual(login_request.status_code, status.HTTP_200_OK)

    # TODO: test read
    # TODO: test update