from django.contrib import admin
from .models import *

class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('slug', 'title')

class ExpensesCateogryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title',)
    list_display_link = ('slug', 'title',)
    search_fields = ('slug', 'title')

class SalaryCategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'amount_usd')
    list_display_link = ('slug', 'title', 'amount_usd')
    search_fields = ('slug', 'title', 'amount_usd')
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('income_category', 'amount_usd', 'amount_kgz', 'rate')
    list_display_link = ('income_category', 'amount_usd', 'amount_kgz', 'rate')
    list_filter = ('amount_usd', 'amount_kgz', 'income_category', 'who_accepted')
    search_fields = ('date', )

class ExpensesAdmin(admin.ModelAdmin):
    list_display = ('expenses_category', 'amount_usd', 'amount_kgz', 'rate')
    list_display_link = ('expenses_category', 'amount_usd', 'amount_kgz', 'rate')
    list_filter = ('amount_usd', 'amount_kgz', 'expenses_category', 'who_accepted')
    search_fields = ('date', )

class AccrualAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount_usd', 'amount_kgz', 'note')
    list_display_link = ('date', 'amount_usd', 'amount_kgz')
    list_filter = ('date', 'amount_kgz', 'amount_usd')
    search_fields = ('date', )

class SalaryPaymentAdmin(admin.ModelAdmin):
    list_display = ('staff', 'full_name', 'salary_category', 'amount_usd')
    list_display_link = ('staff', 'full_name', 'salary_category', 'amount_kgz')
    list_filter = ('staff', 'salary_category', 'amount_usd')
    search_fields = ('full_name', 'staff', )

admin.site.register(IncomeCategory, IncomeCategoryAdmin)
admin.site.register(ExpensesCategory, ExpensesCateogryAdmin)
admin.site.register(SalaryCategory, SalaryCategoryAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(Expenses, ExpensesAdmin)
admin.site.register(Accrual, AccrualAdmin)
admin.site.register(SalaryPayment, SalaryPaymentAdmin)

