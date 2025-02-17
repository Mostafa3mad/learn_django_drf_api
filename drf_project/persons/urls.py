from django.urls import path , include
from .views import PersonViewSet


urlpatterns = [
    path('api/v1/persons/', PersonViewSet.as_view({'get': 'list'})),
]