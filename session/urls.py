from .views import *
from django.urls import path, include

urlpatterns = [
    path('session-list/', SessionListView.as_view(), name='session'),
]