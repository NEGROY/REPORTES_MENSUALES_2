from django.db import models
from .empresas_catalogo import EmpresasCatalogo

class PagReporte(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(
        EmpresasCatalogo,
        on_delete=models.DO_NOTHING,
        db_column="id_cliente"
    )

    cliente = models.CharField(max_length=200)
    paginas = models.JSONField()  # ejemplo: [1,2,3,7,9]
    estado = models.BooleanField(default=True)

    class Meta:
        db_table = "pag_reporte"

#  ORDEN DE LAS PAGINAS QUE TENDRAN LOS REPORTES 
# DE PREFERENCIA LO DEL TEXTO EN JSON 
# 73	WALLMART 	{1,2,3,4,5,6,8,9,10,7,11,12}

