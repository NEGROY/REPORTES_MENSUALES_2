
from django.contrib import admin
from django.urls import path, include
## {{AGREGAMOS EL ESTATICS PARA LA carpeta de statics se puede eliminar  }}
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ADMIN --> proxy 
    path('admin/', admin.site.urls),
    
    # Legacy / transitorio
    path('reporte/', include('app.urls')),
    # path('', include('app.urls')),  TOMAR EN CUENTA QUE ESTA RUTA ES PARA LOS REPORTES 

    # Núcleo del portal
    path('', include('cnoc_app.urls')), # todas las URLs de la app
    #path('cnoc/', include('cnoc_app.urls')),  # RUTAS DEL NUEVO MODUILO 

    # ESCALACIONES 
    path('tablas/', include('escalacion.urls')),
    # ASIENTOS
    # RETRO
]

## YA NO SE USA 
##if settings.DEBUG:
##    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / 'static')