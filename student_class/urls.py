from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register(r'class_category', ClassCategoryViewset)
router.register(r'class', ClassViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('parse_category/', ParseCategory.as_view()),
]