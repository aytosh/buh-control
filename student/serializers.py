from rest_framework import serializers
from .models import Student, FamilyMember
from fee.serializers import FeeSerializer, PaymentSerializer

class StudentSerializer(serializers.ModelSerializer):
    student_id = serializers.ReadOnlyField()

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        student = Student.objects.create(**validated_data)
        student.create_student_id()
        student.save()
        return student

class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'

class StudentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["family_members"] = FamilyMemberSerializer(instance.family_members.all(),
                                                                  context=self.context,
                                                                  many=True).data
        representation["fee"] = FeeSerializer(instance.fees.all(),
                                              context=self.context,
                                              many=True).data
        representation["payments"] = PaymentSerializer(instance.payments.all(),
                                                       context=self.context,
                                                       many=True).data
        return representation


