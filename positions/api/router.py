from rest_framework.routers import DefaultRouter
from positions.api.views import PositionsViewSet, AlcaldiasViewSet

router_positions = DefaultRouter()


router_positions.register(prefix='positions', basename='positions', viewset= PositionsViewSet)
router_positions.register(prefix='alcaldias', basename='alcaldias',viewset= AlcaldiasViewSet)
#router_alcaldias.register(prefix='alcaldias', basename='alcalidas', viewset= AlcaldiasViewSet)
