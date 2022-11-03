from rest_framework import permissions
from rest_framework.views import Request, View


class IsSuperuserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser or request.method == 'GET')
