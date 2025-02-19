from rest_framework_simplejwt.tokens import RefreshToken
from rest_registration.api.serializers import DefaultRegisterUserSerializer,DefaultLoginSerializer

class CustomRegisterUserSerializer(DefaultRegisterUserSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        refresh = RefreshToken.for_user(instance)
        data["refresh"] = str(refresh)
        data["access_token"] = str(refresh.access_token)
        data.pop('password', None)
        return data
