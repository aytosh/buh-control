from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from account.permissions import PermissionMixinAdmin, PermissionMixinAdminAccountant
from .serializers import ClassSerializer, ClassCategorySerializer, RetrieveClassSerializer
from .models import Class, ClassCategory

class ClassCategoryViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = ClassCategory.objects.all()
    serializer_class = ClassCategorySerializer

class ClassViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = RetrieveClassSerializer(instance)
        return Response(serializer.data)


