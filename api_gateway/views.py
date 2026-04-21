
from core.services.cnoc import (
    CronologiaService,
    HistorialDiarioService,
    BusquedaTkService,
    UltimoSeguimientoService,
    TicketsCnocService
)

# CronologiaService , HistorialDiarioService
from core.views.base_json_view import BaseJsonView


class CnocCronologiaApiView(BaseJsonView):
    service_class = CronologiaService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)

        return {
            'ticket': data.get('ticket') or data.get('falla_id', ''),
        }

# ****************************************************************************************************
# Endpoint 12: # Sumatoria de consultas realizadas cada cierta cantidad de tiempo 
#  TOTAL DE CONSULTAS REALIZADAS
# -+--------------------------------------------------------
# modelo de entrada
class CnocHistorialDiarioApiView(BaseJsonView):
    service_class = HistorialDiarioService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)

        return {
            'operador': data.get('operador', ''),
            'fecha_inicio': data.get('fecha_inicio', ''),
            'fecha_fin': data.get('fecha_fin', ''),
        }

# ------------------------------
# Endpoint 11: # http://127.0.0.1:8080/buscar_tk/F6433510
# /*  http://127.0.0.1:8000/api/cnoc/busqueda-tk/F6433510/  */
# ------------------------------
class CnocBusquedaTkApiView(BaseJsonView):
    service_class = BusquedaTkService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)

        return {
            'falla_id': kwargs.get('falla_id') or data.get('falla_id', ''),
        }

# ------------------------------
# Endpoint 9
# http://127.0.0.1:8000/api/cnoc/ultimo_seguimeinto/
# ------------------------------
class CnocUltimoSeguimientoApiView(BaseJsonView):
    service_class = UltimoSeguimientoService


# http://127.0.0.1:8000/api/cnoc/tickets/
class CnocTicketsApiView(BaseJsonView):
    service_class = TicketsCnocService



#


#


#


#


#