from core.queries.oracle.masivas import MasivasListQuery

from .base_masivas_service import BaseMasivasService

# PRINCIPALMENTE UTILIZADO EN LA TABLAS DE ESCALACION    
#  $url = "http://172.20.97.102:8503/masivas/list/{$fallaID}?token=masivas2025"; // ← cambia esto a la URL real

########################################################################################################################
#                                             LISTA LAS FALLAS OPEN MASIVAS                 
# http://127.0.0.1:8000/api/masivas/list/F6433510/
class MasivasListService(BaseMasivasService):
    query_class = MasivasListQuery

    def execute(self):
        falla_id = self.kwargs.get('id', '')

        if not falla_id:
            return self.build_error_response('Debe enviar el ticket masivo.')

        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar tickets asociados a la masiva.',
                result.get('error')
            )

        if not result:
            return self.build_error_response('Ticket no encontrado.')

        return self.build_success_response(result)