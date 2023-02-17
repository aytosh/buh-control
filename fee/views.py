from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from account.permissions import *
from .serializers import *
from .models import *
from account.permissions import *
class DiscountViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()

class FeeCategoryViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    serializer_class = FeeCategorySerializer
    queryset = FeeCategory.objects.all()
 

class FeeViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    serializer_class = FeeSerializer
    queryset = Fee.objects.all()

class PaymentPlanViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    serializer_class = PaymentPlanSerializer
    queryset = PaymentPlan.objects.all()

class PaymentCategoryViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    serializer_class = PaymentCategorySerializer
    queryset = PaymentCategory.objects.all()

class PaymentTypeViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()


class PaymentViewset(PermissionMixinAdminAccountant, viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


