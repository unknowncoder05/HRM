"""Utils for api testing"""

# Django
from django.forms.models import model_to_dict


# Utilities
from enum import Enum
import random


class enumproperty(object):
    "like property, but on an enum class"

    def __init__(self, fget):
        self.fget = fget

    def __get__(self, instance, ownerclass=None):
        if ownerclass is None:
            ownerclass = instance.__class__
        return self.fget(ownerclass)

    def __set__(self, instance, value):
        raise AttributeError("can't set pseudo-member %r" % self.name)

    def __delete__(self, instance):
        raise AttributeError("can't delete pseudo-member %r" % self.name)


class CustomEnum(Enum):
    @enumproperty
    def RANDOM(cls):
        return random.choice(list(cls.__members__.values()))


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
    
    def count(self): # requires object to have non_deleted method
        return self.model_factory.Meta.model.non_deleted.count()

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
        print(f'force create attributes: {data}')  # if action fails, this would help debug

        return instance, data

    def retrive(self, object_id, path=''):
        request_path = f'{self.api_base_route}{path}/{object_id}/'
        print(f'retrive path: {request_path}')  # if action fails, this would help debug

        return self.client.get(request_path, format='json')
    
    def list(self, path=''):
        request_path = f'{self.api_base_route}{path}/'
        print(f'list path: {request_path}')  # if action fails, this would help debug

        return self.client.get(request_path, format='json')
    
    def patch(self, object_id, fields={}, random_fields={}, path=''):
        data = fields.copy()
        request_path = f'{self.api_base_route}{path}/'
        if object_id != None:
            request_path += f'{object_id}/'
            
        print(f'update path: {request_path}')  # if action fails, this would help debug
        print(f'update attributes: {data}')  # if action fails, this would help debug

        return self.client.patch(request_path, data, format='json'), data

    def delete(self, object_id, path=''):
        request_path = f'{self.api_base_route}{path}/'
        if object_id != None:
            request_path += f'{object_id}/'
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
        elif action['method'] == 'patch':
            response = self.patch(**merged_method_kwargs)
        elif action['method'] == 'delete':
            response = self.delete(**merged_method_kwargs)

        if action['callback']:
            return action['callback'](response, **callback_kwargs)

        return response