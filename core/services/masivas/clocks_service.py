from core.queries.oracle.masivas import ClocksFallaQuery

from .base_masivas_service import BaseMasivasService

#######################################################################################################################
#                                             INICIO RELOJES TICKETS                                                    
#                               http://127.0.0.1:8000/api/masivas/clocks/F6433510/#  
#######################################################################################################################
class ClocksFallaService(BaseMasivasService):
    query_class = ClocksFallaQuery

    def execute(self):
        falla = self.kwargs.get('falla', '')

        if not falla:
            return self.build_error_response('Debe enviar la falla.')

        result = self.run_select()

        if isinstance(result, dict) and result.get('error'):
            return self.build_error_response(
                'Error al consultar clocks.',
                result.get('error')
            )

        if not result:
            return self.build_error_response('Falla no encontrada.')

        return self.build_success_response(result)