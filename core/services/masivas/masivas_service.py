from core.queries.oracle.masivas import MasivasQuery

from .base_masivas_service import BaseMasivasService

########################################################################################################################
#       http://127.0.0.1:8000/api/masivas/     """Obtiene listado de tickets masivos abiertos."""
class MasivasService(BaseMasivasService):
    query_class = MasivasQuery

    def execute(self):
        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar masivas.',
                result.get('error')
            )

        return self.build_success_response(result)