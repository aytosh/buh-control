from django.contrib import admin
from .models import *
# Register your models here.

class NationalityAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('staff', 'title')
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('staff', 'title')
class CitizenshipAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('staff', 'title')

class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('staff', 'title')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'specialty')
    list_display_link = ('first_name', 'last_name', 'position', 'specialty')
    list_filter = ('position', 'specialty', 'status')
    search_fields = ('first_name', 'last_name')

class StaffContactInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'phone_number')
    list_display_link = ('user', 'email', 'phone_number')
    search_fields = ('user', )


admin.site.register(Nationality, NationalityAdmin)
admin.site.register(MaritalStatus, MaritalStatusAdmin)
admin.site.register(Citizenship, CitizenshipAdmin)
admin.site.register(Specilaty, SpecialtyAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(StaffContactInfo, StaffContactInfoAdmin)