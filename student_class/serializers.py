from rest_framework import serializers
from .models import *

class ClassCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassCategory
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class RetrieveClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'



