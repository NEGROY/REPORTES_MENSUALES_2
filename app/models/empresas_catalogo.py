from django.db import models

class EmpresasCatalogo(models.Model):

    # OPCIONES DE PAÍS
    PAISES = [ ('GT', 'Guatemala'), ('ESV', 'El Salvador'), ('HN', 'Honduras'), ('CR', 'Costa Rica'), ('NI', 'Nicaragua'), ('CENAM', 'Centroamérica'),]
    #OPCIONES PARA LOS TIPOS MENSUALES XT Banrural CNAM 
    TIPOS = [ ('MENSUALES', 'Mensuales'), ('XT', 'XT'), ('BANRURAL', 'Banrural'), ('CNAM', 'CNAM'), ]

    COD = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=200, null=True, blank=True)
    tt_sitioa = models.IntegerField(null=True, blank=True, help_text="Total de sitios o enlaces monitoreados" ) #TOTAL DE SITIOS || ENLACES MONITOREADOS
    pais = models.CharField(max_length=10, choices=PAISES, null=True)
    STATUS = models.IntegerField(null=True  )  # 0 inactivo / 1 activo
    ORDEN = models.IntegerField(null=True   )  # COMO SE ENVIA EL CORREO
    donde = models.TextField( null=True, help_text="Condición WHERE para los tickets (where_tk + filtros desde sql_base)" )  # WHERE DE LA CONSULTA
    parque_where = models.TextField(null=True, blank=True, help_text="PARQUE DE SERVICIO" )

    tipo = models.CharField( max_length=20, choices=TIPOS    )
    class Meta:
        db_table = "empresas_catalogo"

    def __str__(self):
        return f"{self.razon_social}"

# TABLA PADRE
# esta tabla contiene informacion de los clientes y nombrados por razones sociuales 
# ES UTILIDA en las demas tablas, TIEN EL TOTAL DE SITIOS O ENLACES MONITOREADOS DE LOS CLIENTES 
#  donde = where_tk || desde sql_base  
# WHERE_PARQUE DE SERVICIO  en la de historico_de_indicadores