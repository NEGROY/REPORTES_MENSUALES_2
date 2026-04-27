from ..models import EscalacionArea


# defiunimos lista de areas de escalacion por pAis 
def listar_areasXpais(pais_id: int) -> list[dict]:
    areas=(
        EscalacionArea.objects
        .filter(pais_id=pais_id, activo=True)
        .order_by("nombre_area")
        .values("id", "nombre_area")
    )

    return list(areas)

# OTRAS 



# OTRAS 



# consultas ORM del módulo
# lógica de negocio
# unión de datos API + BD
# funciones como:
# 
# listar áreas por país
# buscar falla
# obtener tabla de escalación