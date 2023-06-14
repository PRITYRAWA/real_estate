import django.contrib.auth.password_validation as validators
from django.contrib.auth import authenticate
from django.core import exceptions
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers
from foundation.models import CustomUser
from api.foundation.exceptions import (AccountDisabledException, InvalidCredentialsException,ExistEmailrException,RequiredException)

class RegistrationSerializer(serializers.Serializer):
    """
    Serializer for register a new user.
    """
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    phone_number = PhoneNumberField(required=False)
    password = serializers.CharField(write_only=True, style={"input_type": "password"})
   
    def _validate_email(self, email):
        # Unique validation
        user = CustomUser.objects.filter(email=email).exists()
        if user:
            raise ExistEmailrException()

        return email

    def _validate_password(self, user, password):
        errors = dict()
        try:
            # validate the password and catch the exception
            validators.validate_password(password=password, user=user)

        # the exception raised here is different than serializers.ValidationError
        except exceptions.ValidationError as e:
            errors["password"] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return password

    def validate(self, validated_data):
        email = validated_data.get("email", None)
        password = validated_data.get("password", None)

        if not email:
            raise RequiredException()

        if not password:
            raise RequiredException()

        # validate user email
        self._validate_email(email)

        # validate password
        user = CustomUser(email=validated_data["email"], password=validated_data["password"])
        self._validate_password(user, password)

        # validate two_step_verification
        self._validate_two_step(validated_data)

        return validated_data

    def create(self, validated_data):
        user = CustomUser.objects.create(
            name=validated_data["name"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])
        user.save()

        return user

class LoginSerializer(serializers.Serializer):
    """
    Serializer to login users with email and password.
    """

    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def _validate_user(self, email, password):
        user = None

        if email and password:
            user = authenticate(username=email, password=password)

        else:
            raise serializers.ValidationError(_("Enter an email and password."))

        return user

    def validate(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")

        user = None

        user = self._validate_user(email, password)

        if not user:
            raise InvalidCredentialsException()

        if not user.is_active:
            raise AccountDisabledException()

        validated_data["user"] = user

        return validated_data


class LogoutSerializer(serializers.Serializer):
    """
    Serializer for logout
    """

    refresh_token = serializers.CharField()