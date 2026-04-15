from django.db import models
from cnoc_app.models import Usuario

# *******************************************
class Hallazgo(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField()
    f_creacion = models.DateTimeField(auto_now_add=True)
    eliminado = models.BooleanField(default=False)
    usuario = models.ForeignKey(
        Usuario,
        to_field="ibm",
        db_column="USER_IBM",
        on_delete=models.PROTECT
    )
    class Meta:
        db_table = "TB_RETRO_HALLAZGO"
    def __str__(self):
        return self.titulo

# *******************************************
class Retroalimentacion(models.Model):
    falla = models.CharField(max_length=100, unique=True)
    assignment = models.CharField(max_length=80, blank=True, null=True)
    hallazgo = models.ForeignKey(
        Hallazgo,
        db_column="id_hallazgo",
        on_delete=models.PROTECT
    )
    update_action = models.TextField(blank=True, null=True)
    variable3 = models.CharField(max_length=80, blank=True, null=True)
    hr_act = models.DateTimeField(blank=True, null=True)
    hr_update = models.DateTimeField(blank=True, null=True)
    seguimiento = models.DateTimeField(blank=True, null=True)
    date_creado = models.DateTimeField(blank=True, null=True)
    usuario = models.ForeignKey(
        Usuario,
        to_field="ibm",
        db_column="USER_IBM",
        on_delete=models.PROTECT
    )
    estado = models.IntegerField()

    class Meta:
        db_table = "TB_RETRO_RETROALIMENTACION"
    def __str__(self):
        return self.falla


# *******************************************
class RetroLogs(models.Model):
    falla_id = models.CharField(max_length=100)
    usuario = models.ForeignKey(
        Usuario,
        to_field="ibm",
        db_column="USER_IBM",
        on_delete=models.PROTECT
    )
    fecha_seguimiento = models.DateField()
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    extra = models.CharField(max_length=20, blank=True, null=True)
    hallazgo = models.ForeignKey(
        Hallazgo,
        db_column="id_hallazgo",
        on_delete=models.PROTECT,
        null=True
    )
    class Meta:
        db_table = "TB_RETRO_LOG"
    
    def __str__(self):
        return self.falla_id


# *******************************************
class Tomados(models.Model):
    ticket = models.CharField(max_length=50)
    ventana = models.CharField(max_length=50)
    usuario = models.ForeignKey(
        Usuario,
        to_field="ibm",
        db_column="ibm_usu",
        on_delete=models.PROTECT
    )
    hora = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)
    extra = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        db_table = "TB_RETRO_TOMADO"  

    def __str__(self):
        return self.ticket

