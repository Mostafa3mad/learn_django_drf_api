# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import CustomUser
# from django.contrib.auth import authenticate, login, logout
# from .serializer import UserSerializer
# from rest_framework_simplejwt.tokens import RefreshToken
# import random
#
#
# class UserCreateView(APIView):
#
#     def post(self, request):
#             # الحصول على البيانات من الـ request بشكل منفصل
#             data = request.data
#             first_name = data.get('first_name')
#             last_name = data.get('last_name')
#
#             # إنشاء الـ username من first_name و last_name
#             username = f"{first_name.lower()}{last_name.lower()}"
#
#             # التحقق إذا كان الـ username موجود في قاعدة البيانات
#             while CustomUser.objects.filter(username=username).exists():
#                 random_number = random.randint(1000, 9999)
#                 username = f"{first_name.lower()}{last_name.lower()}{random_number}"
#             required_fields = ['first_name', 'last_name', 'email', 'password', 'phone_number', 'age', 'gender']
#             missing_fields = [field for field in required_fields if field not in data]
#
#             if missing_fields:
#                 return Response({
#                     'message': f'Missing fields: {", ".join(missing_fields)}'
#                 }, status=status.HTTP_400_BAD_REQUEST)
#
#             serializer = UserSerializer(data=data)
#
#             if serializer.is_valid():
#                 serializer.validated_data['username'] = username
#                 user = serializer.save()
#                 refresh = RefreshToken.for_user(user)
#
#                 return Response({
#                     'message': 'User created successfully',
#                     'user': UserSerializer(user).data,
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token)
#                 }, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
#
# RegiserUser_view = UserCreateView.as_view()
#
