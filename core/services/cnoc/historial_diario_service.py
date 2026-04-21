from datetime import datetime

from core.queries.oracle.cnoc import HistorialDiarioQuery

from .base_cnoc_service import BaseCnocService


class HistorialDiarioService(BaseCnocService):
    query_class = HistorialDiarioQuery

    def execute(self):
        operador = self.kwargs.get('operador', '')
        fecha_inicio = self.kwargs.get('fecha_inicio', '')
        fecha_fin = self.kwargs.get('fecha_fin', '')

        error = self._validate(operador, fecha_inicio, fecha_fin)
        if error:
            return self.build_error_response(error)

        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar el historial diario.',
                result.get('error')
            )

        if not result:
            return self.build_error_response('No hay registros.')

        return self.build_success_response(
            result,
            'Historial diario obtenido correctamente.'
        )

    def _validate(self, operador: str, fecha_inicio: str, fecha_fin: str):
        if not operador:
            return 'El campo operador es obligatorio.'

        if not fecha_inicio:
            return 'El campo fecha_inicio es obligatorio.'

        if not fecha_fin:
            return 'El campo fecha_fin es obligatorio.'

        try:
            dt_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d')
            dt_fin = datetime.strptime(fecha_fin, '%Y-%m-%d')
        except ValueError:
            return 'Las fechas deben tener formato YYYY-MM-DD.'

        if dt_inicio > dt_fin:
            return 'fecha_inicio no puede ser mayor que fecha_fin.'

        return None