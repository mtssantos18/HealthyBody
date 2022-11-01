from rest_framework import permissions
from rest_framework.views import Request, View


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True
        return bool(request.user and request.user.is_staff or request.method == 'GET')
