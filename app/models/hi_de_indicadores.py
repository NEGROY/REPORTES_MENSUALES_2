from django.db import models
from .empresas_catalogo import EmpresasCatalogo

class HiDeIndicadores(models.Model):
    id_cliente = models.ForeignKey(
        EmpresasCatalogo,
        on_delete=models.DO_NOTHING,
        db_column="id_cliente"
    )
    mes = models.IntegerField()
    ano = models.IntegerField()
    inci_menor_o_8 = models.FloatField(null=True, blank=True)
    inci_mayor_a_8 = models.FloatField(null=True, blank=True)
    productividad = models.FloatField(null=True, blank=True)
    sitios_reincidentes = models.FloatField(null=True, blank=True)
    indice_de_reincidencia = models.FloatField(null=True, blank=True)
    mttr_promedio = models.FloatField(null=True, blank=True)
    disponibilidad = models.FloatField(null=True, blank=True)
    proactividad = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "hi_de_indicadores"
        unique_together = ("id_cliente", "mes", "ano")

        