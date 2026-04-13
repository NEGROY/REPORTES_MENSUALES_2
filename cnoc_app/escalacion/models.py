from django.db import models
from cnoc_app.models import Pais, Area
# ************************************************** #


# ********************** TIPO DE ESCALACIÓN **************************** #
class EscalacionTipo(models.Model):
    tipo = models.CharField(max_length=100, unique=True)
    icono = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ESCALACION_TIPO"

    def __str__(self):
        return self.tipo


# ********************** ÁREA DE ESCALACIÓN **************************** #
class EscalacionArea(models.Model):
    nombre_area = models.CharField(max_length=100)
    pais = models.ForeignKey(
        Pais,
        db_column="id_pais",
        on_delete=models.PROTECT
    )
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ESCALACION_AREA"
        indexes = [
            models.Index(fields=["pais"], name="idx_esc_area_pais"),
            models.Index(fields=["activo"], name="idx_esc_area_activo"),
        ]

    def __str__(self):
        return self.nombre_area


# ********************** CONTACTOS DE ESCALACIÓN **************************** #
class EscalacionContacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    centro = models.CharField(max_length=50, blank=True, null=True)
    comentario = models.CharField(max_length=50, blank=True, null=True)
    supervisor = models.BooleanField(default=False)

    pais = models.ForeignKey(
        Pais,
        db_column="id_pais",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ESCALACION_CONTACTO"

    def __str__(self):
        return self.nombre


# ********************** ESCALACIÓN **************************** #
class Escalacion(models.Model):
    nivel = models.CharField(max_length=5)

    tipo_contacto = models.ForeignKey(
        EscalacionContacto,
        db_column="tipo_contacto",
        on_delete=models.PROTECT
    )

    tiempo = models.CharField(max_length=50)

    area = models.ForeignKey(
        EscalacionArea,
        db_column="id_area",
        on_delete=models.PROTECT
    )

    tipo_escalacion = models.ForeignKey(
        EscalacionTipo,
        db_column="id_tipo_escalacion",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    comentario = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "TB_ESCALACION"


# ********************** REGISTRO DE ESCALACIÓN **************************** #
class EscalacionRegistro(models.Model):
    falla_id = models.CharField(max_length=20, blank=True, null=True)
    area_id = models.IntegerField()
    titulo = models.TextField(blank=True, null=True)
    nivel = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    tiempo = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    hora_apertura = models.TimeField(blank=True, null=True)
    hora_sumada = models.TimeField(blank=True, null=True)
    tiempo_acumulado = models.TimeField(blank=True, null=True)
    comentario = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    gestor = models.CharField(max_length=50)
    close_time = models.DateTimeField(blank=True, null=True)
    open_time = models.DateTimeField(blank=True, null=True)
    user = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = "TB_ESCALACION_REGISTRO"


# ********************** FALLA ASOCIADA **************************** #
class EscalacionFallaAsociada(models.Model):
    uniqID = models.CharField(max_length=50, unique=True)
    tk_masiva = models.CharField(max_length=20)
    tk_id = models.CharField(max_length=20)
    enlace = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    close_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    pais = models.CharField(max_length=25, blank=True, null=True)
    pe = models.CharField(max_length=15, blank=True, null=True)
    wan = models.CharField(max_length=15, blank=True, null=True)
    vrf = models.CharField(max_length=50, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    open_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "TB_ESCALACION_FALLA_ASOCIADA"


# ********************** RELOJ DE ESCALACIÓN **************************** #
class EscalacionReloj(models.Model):
    reloj = models.CharField(max_length=100)

    area = models.ForeignKey(
        Area,
        db_column="area",
        on_delete=models.PROTECT
    )

    estado = models.BooleanField(default=True)
    extra = models.BooleanField(default=False)

    class Meta:
        db_table = "TB_ESCALACION_RELOJ"

    def __str__(self):
        return self.reloj


# ********************** BITÁCORA DE ESCALACIÓN **************************** #
class EscalacionBitacora(models.Model):
    user = models.CharField(max_length=30)
    date_update = models.DateTimeField(auto_now_add=True)
    accion = models.CharField(max_length=50)
    observaciones = models.TextField()
    tiempo = models.TimeField(blank=True, null=True)
    tipo = models.CharField(max_length=10, default="0")
    falla = models.CharField(max_length=20, default="F00000")
    correlativo = models.CharField(max_length=50, default="0")
    reloj = models.IntegerField(default=0)

    class Meta:
        db_table = "TB_ESCALACION_BITACORA"