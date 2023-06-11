from rest_framework import viewsets
from .serializer import CitaSerializer
from .models import Cita
# Create your views here.


class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()
