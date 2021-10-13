from hrm_api.users.factories import UserFactory, ProfileFactory
from hrm_api.utils.models import save_save

def user_generator(amount:int):
    users = []
    for user_id in range(amount):
        user = UserFactory()#(username='name'+str(user_id))
        #save_save(user)
        users.append(user)
        ProfileFactory(user=user)
    
    return users