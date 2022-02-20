import imp
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from positions.models import Position
from positions.api.serializers import PositionSerializer, AlcaldiasSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend





    
class PositionsViewSet(ModelViewSet):
    
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
   
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicle_id', 'alcaldia', 'status']

   
class AlcaldiasViewSet(ViewSet):
    
   def list(self, request):
        """Lista las alcaldias disponibles"""
        serializer = AlcaldiasSerializer(Position.objects.all().values("alcaldia").distinct(), many= True)
       


        return Response(status=status.HTTP_200_OK, data=serializer.data)

  
    
    

    
    
    
