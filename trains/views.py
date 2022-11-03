from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from trains.models import Trains
from trains.serializers import TrainSerializer, TrainGetSerializer
from trains.permissions import IsPersonal
# Create your views here.


class CreateListTrainView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPersonal]

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
