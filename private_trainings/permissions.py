from rest_framework import permissions
from rest_framework.views import Request, View
from customers.models import Customer

class MyCustomPermissionCustomer(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj:Customer)->bool:
        try:
            if request.user.customer:
                return request.user.customer == obj and request.method != "DELETE"
        except AttributeError:
            return request.user.is_superuser

class SuperUserPermission(permissions.BasePermission):
     def has_permission(self, request: Request, view: View)->bool:

      if request.user.is_authenticated and request.user.is_superuser:
        return True

class MyCustomPermissionPersonal(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View)->bool:
        ...