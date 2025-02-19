from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.core.validators import EmailValidator
from .serveces import validate_phone_number
from .models import CustomUser
import re

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(validators=[EmailValidator()])
    phone_number = serializers.CharField(validators=[validate_phone_number])

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'age', 'gender']

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists.")
        return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value

    def validate_password(self, value):
        if " " in value:
            raise serializers.ValidationError("Password should not contain spaces.")
        if not re.search(r'[A-Za-z]', value):  # Check if password contains letters
            raise serializers.ValidationError("Password must contain at least one letter.")
        if not re.search(r'[0-9]', value):  # Check if password contains numbers
            raise serializers.ValidationError("Password must contain at least one number.")
        if not re.search(r'[$_]', value):  # Check if password contains special characters
            raise serializers.ValidationError("Password must contain at least one special character ($ or _).")
        if len(value) < 8:  # Check password length
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    def validate(self, data):
        # تحقق إذا كانت الحقول المرسلة تحتوي فقط على الحقول المطلوبة
        valid_fields = set(self.Meta.fields)
        received_fields = set(data.keys())

        # التحقق إذا كانت هناك حقول مفقودة
        missing_fields = valid_fields - received_fields
        if missing_fields:
            raise serializers.ValidationError(f"Missing fields: {', '.join(missing_fields)}")

        # التحقق إذا كانت هناك حقول إضافية
        extra_fields = received_fields - valid_fields
        if extra_fields:
            raise serializers.ValidationError(f"Extra fields: {', '.join(extra_fields)}")

        return data

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user
