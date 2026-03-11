from django.db import models

class EmpresasCatalogo(models.Model):

    COD = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=200, null=True, blank=True)
    tt_sitioa = models.IntegerField(null=True, blank=True) #TOTAL DE SITIOS || ENLACES MONITOREADOS
    pais = models.CharField(max_length=100)
    STATUS = models.IntegerField()  # 0 inactivo / 1 activo
    ORDEN = models.IntegerField()           # COMO SE ENVIA EL CORREO
    donde = models.TextField()              # WHERE DE LA CONSULTA
    tipo = models.CharField(max_length=50)  # conexion con indice_reporte

    class Meta:
        db_table = "empresas_catalogo"

    def __str__(self):
        return f"{self.razon_social}"

# TABLA PADRE
# esta tabla contiene informacion de los clientes y nombrados por razones sociuales 
# ES UTILIDA en las demas tablas, TIEN EL TOTAL DE SITIOS O ENLACES MONITOREADOS DE LOS CLIENTES 