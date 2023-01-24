from django.shortcuts import render
from rest_framework import viewsets
from account.permissions import PermissionMixinAdmin, PermissionMixinAdminAccountant

from .serializers import *
from .models import *

class CashobxViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Cashbox.objects.all()
    serializer_class = CashboxSerializer


class IncomeCategoryViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = Cashbox.objects.all()
    serializer_class = IncomeCategorySerializer

class ExpensesCategoryViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = ExpensesCategory.objects.all()
    serializer_class = ExpensesCategorySerializer

class SalaryCategoryViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = SalaryCategory.objects.all()
    serializer_class = SalaryCategorySerializer

class AccrualViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    queryset = Accrual.objects.all()
    serializer_class = AccrualSerializer


class IncomeViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer

class ExpensesViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer

class SalaryPaymentViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = SalaryPayment.objects.all()
    serializer_class = SalaryPaymentSerializer
