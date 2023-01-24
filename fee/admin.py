from django.contrib import admin
from .models import *
# Register your models here.

class DiscountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'amount_usd',)
    list_display_link = ('pk', 'title', 'amount_usd',)
    list_filter = ('amount_usd', )
    search_fields = ('title', )

class FeeCategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'amount_usd',)
    list_display_link = ('pk', 'title', 'amount_usd',)
    list_filter = ('amount_usd', )
    search_fields = ('title', )

class PaymentplanInFee(admin.TabularInline):
    model = PaymentPlan
    fields = ()
    extra = 3
class FeeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student', 'fee_category',)
    list_display_link = ('pk', 'student', 'fee_category',)
    list_filter = ('fee_category', )
    search_fields = ('student', )
    inlines = [
        PaymentplanInFee
    ]

class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = ('pk', 'date', 'amount',)
    list_display_link = ('pk', 'date', 'amount',)
    list_filter = ('date', 'student')
    search_fields = ('student', 'fee')

class PaymentCategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('slug', "title")

class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('slug', "title")

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student', 'fee', "amount_usd", "amount_kgz")
    list_display_link = ('pk', 'student', 'fee',)
    list_filter = ('student', 'payment_category', "payment_type", "date")
    search_fields = ['student', 'who_paid']

admin.site.register(Discount, DiscountAdmin)
admin.site.register(FeeCategory, FeeCategoryAdmin)
admin.site.register(Fee, FeeAdmin)
admin.site.register(PaymentPlan, PaymentPlanAdmin)
admin.site.register(PaymentCategory, PaymentCategoryAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(Payment, PaymentAdmin)