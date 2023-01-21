from rest_framework.permissions import BasePermission
from staff.models import Staff

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
        staff = Staff.objects.get(user=user)
        if staff.position == "director":
            return True

class IsAdminorIsAccountant(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        staff = Staff.objects.get(user=user)
        if staff.position == "staff" or user.is_staff:
            return True