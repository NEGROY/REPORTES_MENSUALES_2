from .select_services import PaisSelectService, AreaPorPaisSelectService


# PUENTE ENTRE EL CONTROLADOR (views) Y Los select PARA EJECUTAR 
class SelectServiceFactory:
    @staticmethod
    def build(select_type, **kwargs):
        services = {
            'paises': PaisSelectService,
            'areas_por_pais': AreaPorPaisSelectService,
        }

        service_class = services.get(select_type)

        if not service_class:
            raise ValueError(f'Select no soportado: {select_type}')

        return service_class(**kwargs)


# CREO QUE AQUI COLOCARE LAS  FUNCIONES para crear 
# LA LOGICA DE LAS TABLAS DE ESCALACION
