# Utils
from hrm_api.users.factories import UserFactory
from hrm_api.utils.testing import TestModelApiHelper

# Users helper
def user_test_helper(client): # TODO: make this a class and each function should inherit
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

    user_model_helper.add_action(
        actions_name='patch_profile',
        actions_method='patch',
        method_kwargs={'path':'/user/profile'}
    )

    return user_model_helper