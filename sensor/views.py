from rest_framework import viewsets
from .models import Sensor
from .serializers import SensorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    @action(detail=True, methods=["post"])
    def toggle_status(self, request, pk=None):
        try:
            sensor = self.get_object()
            sensor.toggle_status()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
