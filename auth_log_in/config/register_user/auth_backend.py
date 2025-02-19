import jwt
from typing import Optional, Sequence, Type
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from rest_registration.auth_token_managers import AbstractAuthTokenManager, AuthToken, AuthTokenNotRevoked
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication as SimpleJWTAuth
import json

class AuthJWTManager(AbstractAuthTokenManager):
    def get_authentication_class(self) -> Type[BaseAuthentication]:
        return JWTAuthentication

    def get_app_names(self) -> Sequence[str]:
        return ["register_user"]

    def provide_token(self, user):
        # توليد التوكنات (refresh و access)
        refresh = RefreshToken.for_user(user)

        # إعداد التوكنات
        token_dict = {
            "refresh": str(refresh),  # تحويل refresh token إلى نص
            "access": str(refresh.access_token)  # تحويل access token إلى نص
        }

        return {
            "refresh": token_dict["refresh"],
            "access": token_dict["access"],
        }

    def revoke_token(self, user, *, token: Optional[AuthToken] = None) -> None:
        raise AuthTokenNotRevoked()


class JWTAuthentication(SimpleJWTAuth):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'bearer':
            return None

        if len(auth) == 1:
            raise AuthenticationFailed("Invalid authorization header. No credentials provided.")
        if len(auth) > 2:
            raise AuthenticationFailed("Invalid authorization header. Credentials string should not contain spaces.")

        token = auth[1].decode()

        try:
            validated_token = self.get_validated_token(token)
        except Exception:
            raise AuthenticationFailed("Invalid or expired token.")

        user = self.get_user(validated_token)
        if not user:
            raise AuthenticationFailed("User not found.")

        return (user, token)
