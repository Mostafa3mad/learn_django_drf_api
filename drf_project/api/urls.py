from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register('employees', views.EmployeeViewSet,basename='employee')


urlpatterns = [
    path('students/', views.studentsView),
    path('students/<int:pk>/', views.studentDetalView, name='studentDetalView'),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('', include(router.urls)),
    path('blogs/', views.blogsView.as_view()),
    path('comments/', views.commentsView.as_view()),
    #######################
    path('comments/<int:pk>/', views.commentDetalView.as_view()),
    path('blogs/<int:pk>/', views.blogDetalView.as_view()),





]
