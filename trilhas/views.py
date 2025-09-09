from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Trilha, Etapa
from .serializers import TrilhaSerializer, EtapaSerializer


class TrilhaViewSet(viewsets.ModelViewSet):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer

class EtapaViewSet(viewsets.ModelViewSet):
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer

    @action(detail=True, methods=['post'])
    def marcar_como_assistido(self, request, pk=None):
        etapa = self.get_object()
        etapa.assistido = True
        etapa.save()
        return Response({'status': 'etapa marcada como assistida'}, status=status.HTTP_200_OK)

# Create your views here.
