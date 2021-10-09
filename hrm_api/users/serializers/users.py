"""Users serializers."""

# Django
from django.contrib.auth import password_validation
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Models
from hrm_api.users.models import User, Profile

# Serializersc
from hrm_api.users.serializers.profiles import ProfileModelSerializer



class UserModelSerializer(serializers.ModelSerializer):
    """User model serializer."""
    profile = ProfileModelSerializer(read_only=True)

    class Meta:
        """Meta class."""
        model = User

        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'birth_date',
                  'phone_number', 'profile']
    
    #def update(self, instance, validated_data):


class UserSignUpSerializer(serializers.ModelSerializer):
    """User sign up serializer."""
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    # Phone number
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: +999999999. Up to 15 digits allowed."
    )
    phone_number = serializers.CharField(validators=[phone_regex])

    # Password
    password = serializers.CharField(min_length=8, max_length=64)
    class Meta:
        """Meta class."""
        model = User

        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'birth_date',
                  'phone_number', 'password' ]
    
    def validate(self, data):
        """Verify passwords match."""
        passwd = data['password']
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Handle user and profile creation."""
        user = User.objects.create_user(**data, is_verified=True)
        Profile.objects.create(user=user)
        # Send verification mail
        return user