from django.shortcuts import render
from rest_framework import viewsets
from account.permissions import PermissionMixinAdmin, PermissionMixinAdminAccountant
from .serializers import *
from .models import *
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

class StaffContactInfoViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = StaffContactInfo.objects.all()
    serializer_class = StaffContactInfoSerializer

class StaffViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


