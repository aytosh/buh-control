from django.contrib import admin
from .models import Session
#
class SessionAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')
    list_display_link = ('slug', 'title')
    search_fields = ('staff', 'title')

admin.site.register(Session, SessionAdmin)
