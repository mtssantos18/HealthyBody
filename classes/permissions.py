from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            if request.method == "POST":
                return request.user.is_authenticated and request.user.teacher
        except AttributeError:
            return False

        return request.method in permissions.SAFE_METHODS