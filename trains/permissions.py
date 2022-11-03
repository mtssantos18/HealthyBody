from rest_framework import permissions


class IsPersonal(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == "GET" and request.user.customer:
                return True
            if request.user.personal:
                return request.user.personal
        except AttributeError:
            return request.user.is_superuser
