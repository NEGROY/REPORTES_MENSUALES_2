from django.db import models
from cnoc_app.models import Pais, Area, Usuario

# =========================
# MATRIZ (AHORA ES DE ASIENTOS)
# =========================
class Matriz(models.Model):
    sector = models.CharField(max_length=5)
    filas = models.IntegerField()
    columnas = models.IntegerField()
    estado = models.BooleanField()
    creado = models.IntegerField()
    class Meta:
        db_table = "TB_ASIENTO_MATRIZ"

    def __str__(self):
        return self.sector


# =========================
# ASIENTO
# =========================
class Asiento(models.Model):
    matriz = models.ForeignKey(
        Matriz,
        db_column="matiz",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    fila = models.IntegerField()
    columna = models.IntegerField()
    color = models.CharField(max_length=32, blank=True, null=True)
    estado = models.CharField(
        max_length=15,
        choices=[
            ("disponible", "disponible"),
            ("bloqueado", "bloqueado"),
            ("mantenimiento", "mantenimiento"),
        ],
        default="disponible",
    )
    area = models.ForeignKey(
        Area,
        db_column="area_id",
        on_delete=models.PROTECT
    )
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ASIENTO"
         
        constraints = [
            models.UniqueConstraint(
                fields=["area", "matriz", "fila", "columna"],
                name="uq_asiento_posicion"
            )
        ]

    def __str__(self):
        return f"{self.area} [{self.fila},{self.columna}]"


# =========================
# ASIGNACIÓN DE ASIENTO
# =========================
class AsignacionAsiento(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        to_field="ibm",
        db_column="usuario_id",
        on_delete=models.PROTECT
    )
    asiento = models.ForeignKey(
        Asiento,
        db_column="asiento_id",
        on_delete=models.PROTECT
    )
    area = models.ForeignKey(
        Area,
        db_column="area_id",
        on_delete=models.PROTECT
    )
    isoweek = models.SmallIntegerField()
    isoyear = models.SmallIntegerField()
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

    estado = models.CharField(
        max_length=10,
        choices=[("tomado", "tomado"), ("libre", "libre")],
        default="tomado",
    )

    fecha = models.DateField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ASIENTO_ASIGNACION"
         


# =========================
# HORARIO USUARIO (AHORA DE ASIENTOS)
# =========================
class HorarioUsuario(models.Model):
    usuario = models.ForeignKey(
        Usuario,
        to_field="ibm",
        db_column="usuario_id",
        on_delete=models.PROTECT
    )

    dia_semana = models.SmallIntegerField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    estado = models.CharField(
        max_length=10,
        choices=[("activo", "activo"), ("inactivo", "inactivo")],
        default="activo"
    )
    
    tipo = models.CharField(max_length=15, default="Rotativo")
    vigencia_desde = models.DateField()
    vigencia_hasta = models.DateField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ASIENTO_HORARIO_USUARIO"
         
