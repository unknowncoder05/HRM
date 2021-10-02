"""Utils for api testing"""

# Rest Framework
from rest_framework.test import APITestCase, force_authenticate
import datetime

class BaseAPITestCase(APITestCase):
    def count_nondeleted_objects(self, object, *, by_deleted=True, **filters):
        if by_deleted:
            filters['deleted_at'] = datetime.datetime.now()
        return object.objects.filter(**filters).count()