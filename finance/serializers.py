from .models import *
from rest_framework import serializers

class CashboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cashbox
        fields = '__all__'


class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'

class SalaryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryCategory
        fields = '__all__'

class ExpensesCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensesCategory
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

    def create(self, validated_data):
        income = Income.objects.create(**validated_data)
        if income.count_income():
            return income
        else:
            raise serializers.ValidationError("please fill out required fields!")



class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = '__all__'

    def create(self, validated_data):
        expenses = Expenses.objects.create(**validated_data)
        if expenses.count_expenses():
            return expenses

        else:
            raise serializers.ValidationError("please fill out required fields!")

class AccrualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accrual
        fields = '__all__'

    def create(self, validated_data):
        accrual = Accrual.objects.create(**validated_data)
        if accrual.count_accrual():
            return accrual
        else:
            raise serializers.ValidationError("please fill out required fields!")


class SalaryPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryPayment
        fields = '__all__'

    def create(self, validated_data):
        salary_payment = SalaryPayment.objects.create(**validated_data)
        if salary_payment.count_salary():
            return salary_payment
        else:
            raise serializers.ValidationError("please fill out required fields!")

