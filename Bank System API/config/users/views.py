from cmath import phase

from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password





class RegisterUser(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not(username and password and email ):
            return Response({'error':"all fields are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error':"username already exists"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(
                 username=username,
                 email=email,
                 password=make_password(password),
                 )
        serializer = UserSerializer(user)
        refresh = RefreshToken.for_user(user)

        return Response({
            'massage':'success',
            'user':serializer.data,
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        },status=status.HTTP_201_CREATED)
RegisterUserview=RegisterUser.as_view()




