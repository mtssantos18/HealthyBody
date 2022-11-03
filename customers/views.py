from rest_framework import generics
from customers.models import Customer
from customers.serializers import CustomerSerializer
from .permissions import CanNotDeleteCustomerUserDeleted, IsSuperuserAllOrCustomerNotDelete
from rest_framework.authentication import TokenAuthentication
from users.permissions import IsSuperuserOrReadOnly


class CreateListCustomerView(generics.ListCreateAPIView):
    authentication_classes= [TokenAuthentication]
    permission_classes=[IsSuperuserOrReadOnly]

    queryset= Customer.objects.all()
    serializer_class = CustomerSerializer
