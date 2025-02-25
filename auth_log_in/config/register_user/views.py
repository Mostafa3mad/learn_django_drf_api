from rest_framework import viewsets,filters,permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Specialization, CustomUser
from .serializers import SpecializationListSerializer, SpecializationDetailSerializer, DoctorSerializer
from .filters import SpecializationFilter, DoctorFilter
from django_filters.rest_framework import DjangoFilterBackend
from .Pagination import DoctorPagination
class SpecializationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialization.objects.all().order_by('name')
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]  # إضافة البحث والتصفية
    filterset_class = SpecializationFilter
    search_fields = ['name']
    def get_serializer_class(self):
        """استخدام `SpecializationListSerializer` للقائمة و `SpecializationDetailSerializer` عند تحديد تخصص"""
        if self.action == 'list':
            return SpecializationListSerializer
        return SpecializationDetailSerializer

    @action(detail=True, methods=['get'])
    def doctors(self, request, pk=None):
        """إرجاع جميع الأطباء المرتبطين بتخصص معين"""
        specialization = self.get_object()
        doctors = CustomUser.objects.filter(specialization=specialization, role='doctor', is_approved=True)

        filtered_doctors = DoctorFilter(request.GET, queryset=doctors).qs

        if not filtered_doctors.exists():
            return Response({"message": "No approved doctors found for this specialization."}, status=200)

        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    @action(detail=True, methods=['get'], url_path='doctors/(?P<doctor_id>[^/.]+)')
    def doctor_detail(self, request, pk=None, doctor_id=None):
        """إرجاع بيانات طبيب معين داخل تخصص معين"""
        specialization = self.get_object()
        doctor = get_object_or_404(CustomUser, id=doctor_id, specialization=specialization, role='doctor', is_approved=True)

        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)



class DoctorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.filter(role='doctor', is_approved=True)
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = DoctorFilter
    search_fields = ['specialization__name', 'location']




