from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from .serveces import validate_phone_number


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[EmailValidator()])
    phone_number = serializers.CharField(validators=[validate_phone_number])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'age', 'gender']


    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return value


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user