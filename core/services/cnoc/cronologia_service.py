from core.queries.oracle.cnoc import CronologiaQuery

from .base_cnoc_service import BaseCnocService


class CronologiaService(BaseCnocService):
    query_class = CronologiaQuery

    def execute(self):
        ticket = self.kwargs.get('ticket', '')

        if not ticket:
            return self.build_error_response('Debe enviar el ticket.')

        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar la cronología.',
                result.get('error')
            )

        if not result:
            return self.build_error_response('No se encontró cronología para el ticket.')

        row = result[0]

        data = {
            'ticket': row.get('NUMBER', ''),
            'ultimo_comentario': row.get('ULTIMO_COMENTARIO', ''),
            'open_time': row.get('OPEN_TIME'),
            'close_time': row.get('CLOSE_TIME'),
            'es_abierto': not bool(row.get('CLOSE_TIME')),
        }

        return self.build_success_response(
            data,
            'Cronología obtenida correctamente.'
        )