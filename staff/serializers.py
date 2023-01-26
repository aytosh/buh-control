from rest_framework import serializers
from .models import *


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'

class CitizenshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizenship
        fields = '__all__'

class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = '__all__'

class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specilaty
        fields = '__all__'

class StaffContactInfoSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField()
    class Meta:
        model = StaffContactInfo
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'