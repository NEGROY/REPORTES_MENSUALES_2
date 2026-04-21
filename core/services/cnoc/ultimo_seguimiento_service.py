from core.queries.oracle.cnoc import UltimoSeguimientoQuery

from .base_cnoc_service import BaseCnocService

# http://127.0.0.1:8000/api/cnoc/ultimo_seguimeinto/
class UltimoSeguimientoService(BaseCnocService):
    query_class = UltimoSeguimientoQuery

    def execute(self):
        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar el último seguimiento.',
                result.get('error')
            )

        return self.build_success_response(
            result,
            'Último seguimiento obtenido correctamente.'
        )
