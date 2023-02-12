from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .serializers import *
from .models import *
from .service import LargeResultPagination
from django_filters.rest_framework import DjangoFilterBackend
from staff.models import Staff
from account.permissions import PermissionMixinAdmin, PermissionMixinAdminAccountant


class FamilyMemberViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer

class StudentViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LargeResultPagination
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'patronymic', 'student_id', 'admission_year__slug']
    filterset_fields = ['status', 'gender', 'admission_year']
    ordering_fields = '__all__'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StudentRetrieveSerializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = request.user
        if not user.is_staff:
            staff = Staff.objects.get(user=user)
            if staff.position == "staff":
                class_id = staff.class_id
                q = Student.objects.filter(class_id=class_id)
                queryset = self.filter_queryset(q)
            elif staff.position in ["director", "accountant"] or user.is_staff:
                queryset = self.filter_queryset(self.get_queryset())
            else:
                return Response("you dont have access!")
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = StudentReadSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = StudentReadSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = StudentReadSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = StudentReadSerializer(queryset, many=True)
            return Response(serializer.data)


