from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet


router = DefaultRouter()
router.register('', PersonViewSet, basename='persons')

urlpatterns = [
    path('', include(router.urls)),
]