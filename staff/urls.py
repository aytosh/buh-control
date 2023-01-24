from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'nationality', NationalityViewset)
router.register(r'citizenship', CitizenshipViewset)
router.register(r'marital_status', MaritalStatusViewset)
router.register(r'specialty', SpecialtyViewset)
router.register(r'contact_info', StaffContactInfoViewset)
router.register(r'staff', StaffViewset)

urlpatterns = [
    path('', include(router.urls)),
]