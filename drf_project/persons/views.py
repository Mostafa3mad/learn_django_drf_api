from django.shortcuts import render
from rest_framework import viewsets, generics
from .personserializer import PersonSerializer
from .models import Person
from drf_spectacular.utils import extend_schema

@extend_schema(tags=["persons"])
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
