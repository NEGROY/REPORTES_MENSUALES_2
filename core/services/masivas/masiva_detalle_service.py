from core.queries.oracle.masivas import MasivaDetalleQuery

from .base_masivas_service import BaseMasivasService


########################################################################################################################
#  LIST  @app.get("/masivas/{id}")      """Obtiene detalle de un ticket masivo específico."""
#   http://127.0.0.1:8000/api/masivas/F6147001/     """Obtiene detalle de un ticket masivo específico."""
class MasivaDetalleService(BaseMasivasService):
    query_class = MasivaDetalleQuery

    def execute(self):
        ticket_id = self.kwargs.get('id', '')

        if not ticket_id:
            return self.build_error_response('Debe enviar el ticket masivo.')

        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar el detalle de la masiva.',
                result.get('error')
            )

        if not result:
            return self.build_error_response('Ticket no encontrado.')

        return {
            'message': 'successful connection',
            'data': result,
            'code': 200,
            'ok': True,
        }