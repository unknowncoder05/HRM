"""Complementary serializer to BaseModel."""
from rest_framework import serializers


class BasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class."""

        fields = (
            'id', 'created_at', 'updated_at'
        )