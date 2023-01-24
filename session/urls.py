from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SessionViewset

router = DefaultRouter()
router.register(r'session', SessionViewset)

urlpatterns = [
    path('', include(router.urls)),
]