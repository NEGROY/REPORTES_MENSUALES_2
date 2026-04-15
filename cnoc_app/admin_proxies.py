from escalacion.models import (
    Escalacion,
    EscalacionArea,
    EscalacionContacto,
    EscalacionTipo,
    EscalacionReloj,
)

from asientos.models import (
    Matriz,
    Asiento,
    AsignacionAsiento,
    HorarioUsuario,
)

from retroalimentacion.models import Hallazgo


# ======================================================
# ESCALACIÓN (GRUPO VISUAL)
# ======================================================

class EscalacionProxy(Escalacion):
    class Meta:
        proxy = True
        app_label = "tabla_escalacion"
        verbose_name = "Escalación"
        verbose_name_plural = "Escalaciones"


class EscalacionAreaProxy(EscalacionArea):
    class Meta:
        proxy = True
        app_label = "tabla_escalacion"
        verbose_name = "Área de Escalación"
        verbose_name_plural = "Áreas de Escalación"


class EscalacionContactoProxy(EscalacionContacto):
    class Meta:
        proxy = True
        app_label = "tabla_escalacion"
        verbose_name = "Contacto de Escalación"
        verbose_name_plural = "Contactos de Escalación"


class EscalacionTipoProxy(EscalacionTipo):
    class Meta:
        proxy = True
        app_label = "tabla_escalacion"
        verbose_name = "Tipo de Escalación"
        verbose_name_plural = "Tipos de Escalación"


class EscalacionRelojProxy(EscalacionReloj):
    class Meta:
        proxy = True
        app_label = "tabla_escalacion"
        verbose_name = "Reloj de Escalación"
        verbose_name_plural = "Relojes de Escalación"


# ======================================================
# ASIENTOS (GRUPO VISUAL)
# ======================================================

class MatrizProxy(Matriz):
    class Meta:
        proxy = True
        app_label = "asientos_cnoc"
        verbose_name = "Matriz"
        verbose_name_plural = "Matrices"


class AsientoProxy(Asiento):
    class Meta:
        proxy = True
        app_label = "asientos_cnoc"
        verbose_name = "Asiento"
        verbose_name_plural = "Asientos"


class AsignacionAsientoProxy(AsignacionAsiento):
    class Meta:
        proxy = True
        app_label = "asientos_cnoc"
        verbose_name = "Asignación de Asiento"
        verbose_name_plural = "Asignaciones de Asiento"


class HorarioUsuarioProxy(HorarioUsuario):
    class Meta:
        proxy = True
        app_label = "asientos_cnoc"
        verbose_name = "Horario de Usuario"
        verbose_name_plural = "Horarios de Usuario"


# ======================================================
# RETROALIMENTACIÓN (GRUPO VISUAL)
# ======================================================

class HallazgoProxy(Hallazgo):
    class Meta:
        proxy = True
        app_label = "retroalimentacion"
        verbose_name = "Hallazgo"
        verbose_name_plural = "Hallazgos"


class Retroalimentacion(Hallazgo):
    class Meta:
        proxy = True
        app_label = "retroalimentacion"
        verbose_name = "Retroalimentación"
        verbose_name_plural = "RETRO"
