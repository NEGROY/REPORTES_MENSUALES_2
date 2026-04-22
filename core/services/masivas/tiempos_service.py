from core.queries.oracle.masivas import MasivasTiempoQuery

from .base_masivas_service import BaseMasivasService

##############################################################################################################################
#   FALLAS MASIVAS QUE ESTAN OPEN Y SU TIEMPO TOTAL como reloj                                                       
# http://127.0.0.1:8000/api/masivas/tiempos/#
##############################################################################################################################
class MasivasTiempoService(BaseMasivasService):
    query_class = MasivasTiempoQuery

    def execute(self):
        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar MasivasTiempo.',
                result.get('error')
            )

        return self.build_success_response(result)