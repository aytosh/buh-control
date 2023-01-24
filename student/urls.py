from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'student', StudentViewset)
router.register(r'family_member', FamilyMemberViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('parse_category/', ParseCategory.as_view()),
]