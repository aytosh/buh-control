from rest_framework import serializers
from .models import *
from student.serializers import StudentSerializer
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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["students"] = StudentSerializer(instance.students.all(),
                                                                  context=self.context,
                                                                  many=True).data
        return representation





