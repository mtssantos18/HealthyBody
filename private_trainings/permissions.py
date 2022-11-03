from rest_framework import permissions
from rest_framework.views import Request, View


class MyCustomPermissionCustomer(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        try:
            if request.method == "POST":
                return request.user.is_authenticated and request.user.customer
        except AttributeError:
            return False


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:

        if request.user.is_authenticated and request.user.is_superuser:
            return True


class MyCustomPermissionPersonal(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View) -> bool:
        ...
