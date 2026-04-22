from core.queries.oracle.masivas import FallasMasivasQuery

from .base_masivas_service import BaseMasivasService

##############################################################################################################################
#                                             INICIO DE FALLAS MASIVAS 
# http://127.0.0.1:8000/api/masivas/fallas-masivas/F6600761/
class FallasMasivasService(BaseMasivasService):
    query_class = FallasMasivasQuery

    def execute(self):
        fallas = self.kwargs.get('fallas', '')

        if not fallas:
            return self.build_error_response('Debe enviar una o varias fallas.')

        try:
            result = self.run_select()
        except ValueError as exc:
            return self.build_error_response(str(exc))

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar fallas masivas.',
                result.get('error')
            )

        if not result:
            return self.build_error_response('Falla masiva no encontrada.')

        return self.build_success_response(result)