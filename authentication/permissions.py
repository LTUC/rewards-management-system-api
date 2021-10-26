from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False

class IsTa(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_ta:
            return True
        return False

class IsInstructional(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (request.user.is_ta or request.user.is_superuser) :
            return True
        return False

class IsTaAndReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and
            request.user and
            request.user.is_authenticated
        )