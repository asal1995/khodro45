from abc import ABC

from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from User.models import Customer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = Customer.username
        return token


class LoginSerializer(serializers.Serializer):
    token = MyTokenObtainPairSerializer(many=True, read_only=True)
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        trim_whitespace=False,
        write_only=True
    )


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Customer
        fields = ('username', 'password', 're_password')
        extra_kwargs = {
            'username': {'required': True},
            'password': {'required': True},
            're_password': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = Customer.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        return user


