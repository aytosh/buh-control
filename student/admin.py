from django.contrib import admin
from .models import FamilyMember, Student

class FamilyMemeberInLine(admin.TabularInline):
    model = FamilyMember
    fields = ()
    extra = 1
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'student_id', 'first_name', 'last_name', 'group', 'status')
    list_display_link = ('student_id', 'first_name', 'last_name', 'group')
    list_filter = ('group', 'status', 'gender')
    search_fields = ('student_id', 'first_name', 'last_name')
    inlines = [
        FamilyMemeberInLine
    ]

class FamilyMemeberAdmin(admin.ModelAdmin):
    list_display = ('student', 'fullname', 'who', 'is_responsible')
    list_display_link = ('student', 'full_name', 'who', 'is_responsible')
    list_filter = ('student', 'is_responsible')
    search_fields = ('student', 'full_name', 'id_passport')

admin.site.register(FamilyMember, FamilyMemeberAdmin)
admin.site.register(Student, StudentAdmin)
