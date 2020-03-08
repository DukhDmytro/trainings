from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = 'username', 'password', 'first_name', 'last_name', 'email'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
