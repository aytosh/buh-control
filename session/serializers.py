from rest_framework import serializers
from .models import Session
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

