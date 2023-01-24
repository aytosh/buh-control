from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'cashbox', CashobxViewset)
router.register(r'income_category', IncomeCategoryViewset)
router.register(r'expenses_category', ExpensesCategoryViewset)
router.register(r'salary_category', SalaryCategoryViewset)
router.register(r'accrual', AccrualViewset)
router.register(r'income', IncomeViewset)
router.register(r'expenses', ExpensesViewset)
router.register(r'salary_payment', SalaryPaymentViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('parse_category/', ParseCategory.as_view()),
]