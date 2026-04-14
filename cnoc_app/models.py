from django.db import models
from django.utils import timezone

# MODELOS DE CNOC_APP 
# from cnoc_app.escalacion.models import *

# =========================
# MODELOS MAESTROS (GENERALES)
# =========================

class Area(models.Model):
    nombre_area = models.CharField(max_length=35)
    estado = models.BooleanField(default=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    creado_en = models.DateTimeField(default=timezone.now)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_area"

    def __str__(self):
        return self.nombre_area


class Pais(models.Model):
    nombre_pais = models.CharField(max_length=20, unique=True)
    ext = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tb_pais"

    def __str__(self):
        return self.nombre_pais


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    username2 = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=120, unique=True)
    pass_plain = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=255)
    activo = models.BooleanField(default=True)
    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # area = models.CharField(max_length=50, blank=True, null=True)
    ibm = models.IntegerField(unique=True)
    agente = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    baja = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "tb_usuario"

    def __str__(self):
        return self.username2


# =========================
# CHANGE LOG (AUDITORÍA)
# =========================

class ChangeLog(models.Model):
    entity = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    action = models.CharField(max_length=20)
    payload = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=80, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tb_change_log"
        indexes = [
            models.Index(fields=["entity"]),
            models.Index(fields=["entity_id"]),
            models.Index(fields=["username"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.entity} {self.entity_id} {self.action}"