from django.http import JsonResponse

from blogs.models import Blog,Comment
from employees.models import Employee
from students.models import Student
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView
from rest_framework import status, viewsets
from .serializers import studentSerializer, employeeSerializer
from blogs.Serializer import BlogSerializer,CommentSerializer
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins ,generics
from .Paginations import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter

@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def studentDetalView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except:
        return Response({'detail': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = studentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class Employees(APIView):
#     def get(self,request):
#         employees = Employee.objects.all()
#         serializer = employeeSerializer(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer = employeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class EmployeeDetail(APIView):
#     def get_object(self,pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = employeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = employeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

# mixins
'''
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)



class EmployeeDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''


'''
#Genreric
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
# Genreric
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    
'''
# ModelViewSet
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    pagination_class = CustomPagination
    # filterset_fields = ['designation']
    filterset_class = EmployeeFilter

#Blogs

class blogsView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class commentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class blogDetalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class commentDetalView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer