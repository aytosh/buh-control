from rest_framework import serializers
from .models import *
from .exceptions import CustomException

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

class FeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeCategory
        fields = '__all__'

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'

    def create(self, validated_data):
        fee = Fee.objects.create(**validated_data)
        if fee.count_payment():
            return fee
        else:
            raise CustomException


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["payment_plan"] = PaymentPlanSerializer(instance.payment_plans.all(),
                                                                  context=self.context,
                                                                  many=True).data
        return representation
class PaymentPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentPlan
        fields = '__all__'

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class PaymentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentCategory
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    def create(self, validated_data):
        payment = Payment.objects.create(**validated_data)
        if payment.count_payment():
            return payment
        else:
            raise CustomException
