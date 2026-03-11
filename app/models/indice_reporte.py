from django.db import models


class IndiceReporte(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    MENSUALES = models.BooleanField(default=False)
    XT = models.BooleanField(default=False)
    banrural = models.BooleanField(default=False)
    CNAM = models.BooleanField(default=False)

    class Meta:
        db_table = "INDICE_REPORTE"

    def __str__(self):
        return self.titulo
    
    # ESTA ES TABLA QUE CONTENDRA QUE PAGINAS HAY Y CUALES NO 

#  ID	TITULO	       MENSUALES XT	BANRURAL CENAM
#   1	NOMBRE DE CLIENTE	1	 1	1	1
#   2	Objetivo	        1	 1	1	1
#   3	Monitoreo Proactivo 1	 1	1	1
#   4	Monitoreo Proactivo	0	 1	1	1
#   5	Indicadores	        1	 1	0	1
#   6	Histórico de Indic	1	 0	1	0
#   7	Comportamiento Red  1	 1	1	1
    
