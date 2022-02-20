from rest_framework.serializers import ModelSerializer
from positions.models import Position

class PositionSerializer(ModelSerializer):
    """Validamos los datos de la posición por unidad"""
    class Meta:
        model = Position
        fields = ['vehicle_id', 'alcaldia', 'geographic_point', 'status']



class AlcaldiasSerializer(ModelSerializer):
    """Validamos las alcaldias disponibles"""
    class Meta:
        model = Position
        fields = ['alcaldia']

