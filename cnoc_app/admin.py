from django.contrib import admin
from django.utils.html import format_html
from cnoc_app.admin_proxies import *

# =========================
# TABLAS DE ESCALACION ADMIN 
# =========================

# TABLA DE ESCALACIÓN
@admin.register(EscalacionProxy)
class EscalacionAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        "contacto_nombre",
        "area",
        "nivel",
        "tipo_escalacion",
        "created_at",
    )
    list_filter = (
        "area",
        "nivel",
        "tipo_escalacion",
        "created_at",
    )
    search_fields = (
        "area__nombre_area",
        "tipo_contacto__nombre",
        "comentario",
    )
    ordering = (
        "area__nombre_area",
        "nivel",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related(
            "area",
            "tipo_contacto",
            "tipo_escalacion",
        )

    @admin.display(description="Contacto")
    def contacto_nombre(self, obj):
        return obj.tipo_contacto.nombre

# EscalacionArea # admin.site.register(EscalacionAreaProxy)
@admin.register(EscalacionAreaProxy)
class EscalacionAreaAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("nombre_area", "pais", "activo")
    list_filter = ("pais", "activo")
    search_fields = ("nombre_area",)

# CONTACTOS DE ESCALACIÓN
@admin.register(EscalacionContactoProxy)
class EscalacionContactoAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        "nombre",
        "pais",
        "correo",
        "telefono",
        "supervisor",
    )
    list_filter = (
        "pais",
        "supervisor",
    )
    search_fields = (
        "nombre",
        "correo",
        "telefono",
    )
    ordering = (
        "nombre",
    )

# EscalacionTipo
@admin.register(EscalacionTipoProxy)
class EscalacionTipoAdmin(admin.ModelAdmin):
    actions = None

# RELOJES DE ESCALACIÓN
@admin.register(EscalacionRelojProxy)
class EscalacionRelojAdmin(admin.ModelAdmin):
    actions = None
    list_display = (
        "reloj",
        "area",
        "estado",
        "extra",
    )
    list_filter = (
        "area",
        "estado",
        "extra",
    )
    search_fields = (
        "reloj",
    )
    ordering = (
        "area__nombre_area",
        "reloj",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("area")

# =========================
# ASIENTOS CNOC
# =========================

# MatrizProxy
@admin.register(MatrizProxy)
class MatrizProxyAdmin(admin.ModelAdmin):
    actions = None
    list_display  = ( "sector", "filas", "columnas", "estado" )
    list_filter   = ( "sector" , "estado" ) 
    # search_fields = ( "sector" , "estado" ) 
    ordering =  ("sector", )

# AsientoProxy
@admin.register(AsientoProxy)
class AsientoAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("matriz", "fila", "columna", "area", "estado" )
    list_filter  = ("matriz" , "area" ) 
    ordering     = ("matriz",  )
    
    @admin.display(description="Color")
    def color_preview(self, obj):
        if obj.color:
            return format_html(
                '<div style="width:20px; height:20px; background-color:{}; '
                'border:1px solid #000;"></div>',
                obj.color
            )
        return "-"
  
# AsignacionAsientoProxy
@admin.register(AsignacionAsientoProxy)
class AsignacionAsientoAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("usuario", "asiento", "area", "isoweek" )
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(isoweek=0)

# HorarioUsuarioProxy
@admin.register(HorarioUsuarioProxy)
class HorarioUsuarioAdmin(admin.ModelAdmin):
    actions = None
    list_display = ("usuario", "dia_semana", "estado" )
 

# =========================
# TABLAS DE ESCALACION ADMIN 
# =========================

admin.site.register(HallazgoProxy)