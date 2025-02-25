import django_filters
from django.db.models import Count
from .models import Specialization, CustomUser

class SpecializationFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains', label="Specialization Name")
    min_doctors = django_filters.NumberFilter(method='filter_min_doctor_count', label="Min Doctor Count")  # الحد الأدنى لعدد الأطباء

    class Meta:
        model = Specialization
        fields = ['name']

    def filter_min_doctor_count(self, queryset, name, value):
        """فلترة التخصصات بناءً على الحد الأدنى لعدد الأطباء الموافق عليهم"""
        return queryset.annotate(doctor_count=Count('customuser')).filter(doctor_count__gte=value)

class DoctorFilter(django_filters.FilterSet):
    specialization = django_filters.CharFilter(field_name='specialization__name', lookup_expr='icontains',label="Specialization")
    min_price = django_filters.NumberFilter(field_name='consultation_price', lookup_expr='gte', label="Min Price")  # البحث بالسعر الأدنى
    max_price = django_filters.NumberFilter(field_name='consultation_price', lookup_expr='lte', label="Max Price")  # البحث بالسعر الأعلى
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')  # البحث بالموقع

    class Meta:
        model = CustomUser
        fields = ['specialization', 'min_price', 'max_price', 'location']
