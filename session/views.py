from rest_framework import viewsets
from .models import Session
from .serializers import SessionSerializer
from account.permissions import PermissionMixinAdmin
# Create your views here.
class SessionViewset(PermissionMixinAdmin, viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer


