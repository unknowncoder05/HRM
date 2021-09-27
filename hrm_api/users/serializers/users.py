"""Users serializers."""

# Django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from hrm_api.users.models import User, Profile

# Serializers
from hrm_api.users.serializers.profiles import ProfileModelSerializer



class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        """Meta class."""
        model = User

class UserSignupModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    password = serializers.CharField()
    dob = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        """Meta class."""
        model = User

        fields = ['first_name', 'middle_name', 'last_name', 'email', 'username', 'alias', 'dob', 'private',
                  'phone_number', 'password', 'password_confirmation', ]