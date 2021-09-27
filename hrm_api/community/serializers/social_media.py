"""Link serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from hrm_api.community.models import Link


class LinkModelSerializer(serializers.ModelSerializer):
    """Link model serializer."""

    class Meta:
        """Meta class."""

        model = Link