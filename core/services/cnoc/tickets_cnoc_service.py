from core.queries.oracle.cnoc import TicketsCnocQuery

from .base_cnoc_service import BaseCnocService

# http://127.0.0.1:8000/api/cnoc/tickets/
class TicketsCnocService(BaseCnocService):
    query_class = TicketsCnocQuery

    def execute(self):
        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar tickets CNOC.',
                result.get('error')
            )

        return self.build_success_response(
            result,
            'Tickets CNOC obtenidos correctamente.'
        )