from rest_framework import serializers


def validate_phone_number(value):
    if not value.isdigit():
        raise serializers.ValidationError("Phone number must contain only digits.")
    if len(value) < 10:
        raise serializers.ValidationError("Phone number must be at least 10 digits long.")
    return value
