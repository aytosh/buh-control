from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'discount', DiscountViewset)
router.register(r'fee_category', FeeCategoryViewset)
router.register(r'fee', FeeViewset)
router.register(r'payment_plan', PaymentPlanViewset)
router.register(r'payment_category', PaymentCategoryViewset)
router.register(r'payment_type', PaymentTypeViewset)
router.register(r'payment', PaymentViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('parse_category/', ParseCategory.as_view()),
]