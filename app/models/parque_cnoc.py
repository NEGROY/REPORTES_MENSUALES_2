from django.db import models
from .empresas_catalogo import EmpresasCatalogo

class ParqueCnoc(models.Model):

    id_cliente = models.ForeignKey(
        EmpresasCatalogo,
        on_delete=models.DO_NOTHING,
        db_column="id_cliente"
    )

    mes = models.IntegerField()
    ano = models.IntegerField()
    sitios_activos = models.IntegerField(null=True, blank=True)
    tt_EnlacesDatos = models.IntegerField(null=True, blank=True) # Total de Enlaces de datos 
    internet = models.IntegerField(null=True, blank=True) # Internet
    AE = models.IntegerField(null=True, blank=True)     # AE 
    tt_tt = models.IntegerField(null=True, blank=True)  # Total de TT

    class Meta:
        db_table = "parque_cnoc"
        unique_together = ("id_cliente", "mes", "ano")

# pag 7, Comportamiento de la RED de CLIENTE 
#Comportamiento de la Red del Cliente