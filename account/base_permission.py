from rest_framework.permissions import BasePermission


class IsClientOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'admin':
            return True
        if request.user == obj.owner:
            return True
        if request.user.role == 'client':
            return True
        return False

