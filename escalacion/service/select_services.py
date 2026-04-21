from core.services.base_select_service import BaseSelectService
# MODELOS QUE SEA utilizados 
from cnoc_app.models import Pais
from escalacion.models import EscalacionArea


class PaisSelectService(BaseSelectService):
    model = Pais
    order_by = ('id',)
    fields = ('id', 'nombre_pais')
    filters = {
        'id__gt': 1,
    }


class AreaPorPaisSelectService(BaseSelectService):
    model = EscalacionArea
    order_by = ('nombre_area',)
    fields = ('id', 'nombre_area')
    filters = {
        'activo': True,
    }

    def get_filters(self):
        return {
            **self.filters,
            'pais_id': self.kwargs.get('pais_id'),
        }