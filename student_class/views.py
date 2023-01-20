from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import ClassSerializer, ClassCategorySerializer
from .models import Class, ClassCategory

class ClassCategoryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, ]
    queryset = ClassCategory.objects.all()
    serializer_class = ClassCategorySerializer

class ClassCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser, ]
