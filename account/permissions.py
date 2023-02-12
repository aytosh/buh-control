from rest_framework.permissions import BasePermission
from staff.models import Staff
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class IsActivePermission(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_active)
class IsAccountant(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        staff = Staff.objects.get(user=user)
        if staff.position == "accountant":
            return True

class IsStaff(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        staff = Staff.objects.get(user=user)
        if staff.position == "staff":
            return True

class IsDirector(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.pk:
            staff = Staff.objects.get(user=user)
            if staff.position == "director":
                return True
        else:
            return False

class IsAdminorIsAccountant(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            return True

        elif user.pk:
            staff = Staff.objects.get(user=user)
            if staff.position == "accountant":
                return True
        else:
            return False

class PermissionMixinAdmin:
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdminUser, ]
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]

class PermissionMixinAdminAccountant:
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permissions = [IsAdminorIsAccountant, ]
        else:
            permissions = [IsAuthenticated, ]
        return [permission() for permission in permissions]