from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from trains.models import Trains
from trains.serializers import TrainSerializer, TrainGetSerializer
from trains.permissions import IsPersonalOrCustomerReadOnly
from utils.mixins import SerializerByMethodMixin
# Create your views here.


class CreateListTrainView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPersonalOrCustomerReadOnly]

    queryset = Trains.objects.all()

    serializer_map = {
        "GET": TrainGetSerializer,
        "POST": TrainSerializer,
    }

    def get_queryset(self):
        try:
            if self.request.user.customer:
                return self.queryset.filter(customer=self.request.user.customer)
        except AttributeError:
            return self.queryset.all()


class RetrieveUpdateDestroyTrainView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPersonalOrCustomerReadOnly]

    lookup_url_kwarg = "train_id"

    queryset = Trains.objects.all()
    serializer_class = TrainGetSerializer
