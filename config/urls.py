
from django.contrib import admin
from django.urls import path, include
## {{AGREGAMOS EL ESTATICS PARA LA carpeta de statics se puede eliminar  }}
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # todas las URLs de la app
    path('cnoc/', include('cnoc_app.urls')),  # RUTAS DEL NUEVO MODUILO 

    # ESCALACIONES 
    path('tablero/', include('escalacion.urls')),

    # ASIENTOS

    # RETRO
]

## YA NO SE USA 
##if settings.DEBUG:
##    urlpatterns += static(settings.STATIC_URL, document_root=BASE_DIR / 'static')