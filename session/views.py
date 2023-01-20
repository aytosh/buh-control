from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Session
from .serializers import SessionSerializer
# Create your views here.

class SessionListView(generics.ListAPIView):
    permission_classes = [IsAdminUser, ]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
