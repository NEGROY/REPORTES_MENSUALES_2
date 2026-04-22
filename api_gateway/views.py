# APIS PAR AEL CNOC
from core.services.cnoc import (
    CronologiaService,
    HistorialDiarioService,
    BusquedaTkService,
    UltimoSeguimientoService,
    TicketsCnocService
)
# MASIVAS APIS 
from core.services.masivas import ( 
    MasivasTiempoService,  
    FallasMasivasService, 
    ClocksFallaService,
    MasivasListService, 
    MasivaDetalleService,
    MasivasService, 
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

# **************************************************************************************
# from core.services.masivas.tiempos_service import MasivasTiempoService

##############################################################################################################################
#   FALLAS MASIVAS QUE ESTAN OPEN Y SU TIEMPO TOTAL como reloj                                                       
#   http://127.0.0.1:8000/api/masivas/tiempos/#
##############################################################################################################################
class MasivasTiempoApiView(BaseJsonView):
    service_class = MasivasTiempoService
##############################################################################################################################
#                                             INICIO DE FALLAS MASIVAS                                                       
# http://127.0.0.1:8000/api/masivas/fallas-masivas/F6600761/ #
##############################################################################################################################
class FallasMasivasApiView(BaseJsonView):
    service_class = FallasMasivasService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)

        return {
            'fallas': kwargs.get('fallas') or data.get('fallas', ''),
        }

#######################################################################################################################
#                                             INICIO RELOJES TICKETS                                                  
#                        http://127.0.0.1:8000/api/masivas/clocks/F6433510/#  
#######################################################################################################################
class ClocksFallaApiView(BaseJsonView):
    service_class = ClocksFallaService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)
        return {
            'falla': kwargs.get('falla') or data.get('falla', ''),
        }

########################################################################################################################
#                                             LISTA LAS FALLAS OPEN MASIVAS                 
# http://127.0.0.1:8000/api/masivas/list/F6433510/
class MasivasListApiView(BaseJsonView):
    service_class = MasivasListService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)
        return {
            'id': kwargs.get('id') or data.get('id', ''),
        }

########################################################################################################################
#   http://127.0.0.1:8000/api/masivas/F6147001/     """Obtiene detalle de un ticket masivo específico."""
class MasivaDetalleApiView(BaseJsonView):
    service_class = MasivaDetalleService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)
        return {
            'id': kwargs.get('id') or data.get('id', ''),
        }

########################################################################################################################
#       http://127.0.0.1:8000/api/masivas/     """Obtiene listado de tickets masivos abiertos."""
class MasivasApiView(BaseJsonView):
    service_class = MasivasService

########################################################################################################################