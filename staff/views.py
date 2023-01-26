from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from account.permissions import PermissionMixinAdmin, PermissionMixinAdminAccountant
from .serializers import *
from .models import *
from student.service import LargeResultPagination
# Create your views here.
class NationalityViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

class CitizenshipViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Citizenship.objects.all()
    serializer_class = CitizenshipSerializer

class MaritalStatusViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

class SpecialtyViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Specilaty.objects.all()
    serializer_class = SpecialtySerializer

class NationalityViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

class StaffContactInfoViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = StaffContactInfo.objects.all()
    serializer_class = StaffContactInfoSerializer
    # def perform_create(self, serializer):
    #     user = self.request.user
    #     serializer.save(user=user)
    #
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = super().get_queryset()
    #     staff = Staff.objects.get(user=user)
    #     if staff.position == "staff":
    #         queryset = StaffContactInfo.objects.get(user=user)
    #     return queryset

class StaffViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = LargeResultPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'patronymic', 'username', 'specialty__slug']
    filterset_fields = ['status', 'gender', 'position']
    ordering_fields = '__all__'