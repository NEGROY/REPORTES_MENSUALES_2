from core.queries.oracle.cnoc import BusquedaTkQuery

from .base_cnoc_service import BaseCnocService

# /*  http://127.0.0.1:8000/api/cnoc/busqueda-tk/F6433510/  */
class BusquedaTkService(BaseCnocService):
    query_class = BusquedaTkQuery

    def execute(self):
        falla_id = self.kwargs.get('falla_id', '')

        if not falla_id:
            return self.build_error_response('Debe enviar el ticket.')

        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar el ticket.',
                result.get('error')
            )

        if not result:
            return self.build_error_response(
                f'No se encontró información para el ticket {falla_id}'
            )

        return self.build_success_response(
            result,
            'Ticket obtenido correctamente.'
        )
