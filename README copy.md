APP
└── cnoc_app
    ├── models
    │   ├── retro
    │   ├── tabla_escalacion
    │   └── asientos


app/
└── cnoc_app/
    ├── retro/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    │
    ├── tabla_escalacion/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    │
    ├── asientos/
    │   ├── migrations/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    │
    └── __init__.py



--------------------------------------------------------------------------

✅ OPCIÓN 1 — config COMO ORQUESTADOR DE MÓDULOS (RECOMENDADA)
📌 Qué hace config

Registra cnoc_app
Define rutas globales
Define permisos globales
Define flags de activación
Centraliza settings

📍 Ejemplo en config/settings.py
Python
INSTALLED_APPS = [
    ...
    'cnoc_app',
]
``
``Mostrar más líneas
✅ Correcto
❌ No colocar submódulos aquí (cnoc_app.escalacion NO va aquí)


✅ OPCIÓN 2 — URLs CENTRALIZADAS DESDE config
config/urls.py
urlpatterns = [
    path('cnoc/', include('cnoc_app.urls')),
]

Y cnoc_app gestiona internamente:
cnoc/
├── retroalimentacion/
├── escalacion/
├── asientos/

✅ Esto mantiene orden jerárquico
✅ Facilita versionado futuro (/cnoc/v2/)


✅ OPCIÓN 3 — FLAGS DE ACTIVACIÓN POR MÓDULO (MUY PROFESIONAL)
Puedes usar config/settings.py para habilitar o deshabilitar módulos sin tocar código.

CNOC_MODULES = {
    "RETROALIMENTACION": True,
    "ESCALACION": True,
    "ASIENTOS": True,
}

En cnoc_app/urls.py:

from django.conf import settings

urlpatterns = []

if settings.CNOC_MODULES.get("RETROALIMENTACION"):
    urlpatterns.append(
        path('retroalimentacion/', include('cnoc_app.retroalimentacion.urls'))
    )

Mostrar más líneas
✅ Ideal para entornos productivos
✅ Activar/desactivar por cliente
✅ Muy usado en sistemas corporativos


✅ OPCIÓN 4 — CONFIGURACIÓN ESPECÍFICA DE CNOC AISLADA
Para escalar bien, puedes separar settings:

config/
├── settings.py
├── settings_cnoc.py

En settings.py:
from .settings_cnoc import *

from .settings_cnoc import *Mostrar más líneas
En settings_cnoc.py:

CNOC_SLA_DEFAULT = 240  # minutos
CNOC_ESCALATION_LEVELS = ["L1", "L2", "L3"]
CNOC_ENABLE_AUDIT = True

✅ Limpio
✅ Modular
✅ Preparado para auditoría y SLA




pasos 

AGREGAR SUB MENUS A LOS dropdown DEL NAVBAR

Lo más limpio en Django para un dropdown dinámico es:
1. Definir el menú en Python
2. Resolver URLs en backend
3. Enviar el menú al template con context processor
4. Renderizar con un solo for en navbar.html
Así evitas hardcodear enlaces en HTML y luego puedes agregar permisos sin tocar el template.

****************************************************************************************************
    FRONT END 
        ESCALACIONES 
        ASIENTOS
        RETRO 

****************************************************************************************************
BACKEND 
    MODEALES 
    JS 
    CONSULTAS 

****************************************************************************************************
    TOMAR EN CUENTA LOS ASIENTOS 
    Y PARA EL TABLERO DE ESCALACION 
    QUE SEGUN USUARIOS TENDRAN ALGUNAAS VISTA U OPCIONES 


****************************************************************************************************
MAS ADELNATE PARA EL TABLERO DE ESCLACION 
    Quitar JS mock
    Renderizar cards con:
    {% for item in escalaciones %}
    
****************************************************************************************************
Listado de pasos para incorporar core y mover Oracle correctamente

Crear la carpeta core en la raíz del proyecto.
Crear dentro de core la estructura base para manejo de base de datos externa.
Crear el submódulo específico para Oracle dentro de core.

Agregar los archivos de inicialización necesarios para que Python reconozca los paquetes.
Separar la lógica actual de conexión Oracle del archivo app/service/dboracle.py.
Mover la responsabilidad de conexión a un archivo dedicado dentro de core/db/oracle.
Crear un archivo exclusivo para manejo de cursor y ciclo de vida de conexión.
Crear un archivo exclusivo para consultas Oracle.
Crear un archivo exclusivo para validación o prueba de conectividad Oracle.
    # =========================
# 1) Archivos de inicialización
# =========================
if (!(Test-Path "core\__init__.py")) { New-Item "core\__init__.py" -ItemType File | Out-Null }
if (!(Test-Path "core\db\__init__.py")) { New-Item "core\db\__init__.py" -ItemType File | Out-Null }
if (!(Test-Path "core\db\oracle\__init__.py")) { New-Item "core\db\oracle\__init__.py" -ItemType File | Out-Null }
# =========================
# 2) Archivos dedicados para Oracle
# =========================
if (!(Test-Path "core\db\oracle\connection.py")) { New-Item "core\db\oracle\connection.py" -ItemType File | Out-Null }
if (!(Test-Path "core\db\oracle\cursor.py")) { New-Item "core\db\oracle\cursor.py" -ItemType File | Out-Null }
if (!(Test-Path "core\db\oracle\queries.py")) { New-Item "core\db\oracle\queries.py" -ItemType File | Out-Null }
if (!(Test-Path "core\db\oracle\healthcheck.py")) { New-Item "core\db\oracle\healthcheck.py" -ItemType File | Out-Null }
# =========================
# 3) Mover el archivo actual de Oracle a core como respaldo temporal
# =========================
if (Test-Path "app\service\dboracle.py") {    Move-Item "app\service\dboracle.py" "core\db\oracle\dboracle_legacy.py" -Force }
# =========================
# 4) Verificar estructura final
# =========================
Get-ChildItem "core" -Recurse


Revisar el contenido actual de dboracle.py y clasificar qué pertenece a conexión, qué a consultas y qué a validaciones.
Reubicar cada bloque de código en el archivo correspondiente dentro de core.
Mantener el comando de gestión test_oracle.py en su ubicación actual.
Actualizar el comando de gestión para que consuma la nueva lógica centralizada en core.

Verificar que ninguna app quede dependiendo directamente de la ubicación antigua de Oracle.
Actualizar importaciones internas que actualmente apunten a app/service/dboracle.py.
Revisar si alguna vista, servicio o proceso automático usa la conexión Oracle actual.
Redirigir esas dependencias hacia la nueva estructura centralizada.
Validar que la configuración sensible de Oracle esté centralizada en settings o variables de entorno.

Confirmar que las credenciales y DSN no queden duplicados en varios archivos.
Probar la conectividad desde el nuevo módulo centralizado.
Probar la ejecución del comando de gestión luego del cambio.
Verificar que las consultas Oracle sigan respondiendo igual que antes.
Confirmar que la migración no afecte el resto de apps del proyecto.
Dejar app/service/dboracle.py fuera de uso.
Eliminar o archivar el archivo anterior cuando ya no existan dependencias activas.
Documentar la nueva ubicación oficial de Oracle dentro del proyecto.
Definir la regla arquitectónica para futuras integraciones externas: infraestructura compartida en core.

****************************************************************************************************
        {{Flujo}}
Template / JS / Formulario
        ↓
      urls.py
        ↓
      views.py
        ↓
   services.py   ← aquí decides qué hacer
        ↓
 core/apis/*.py  ← aquí se consume la API externa
        ↓
 API externa

****************************************************************************************************
views.py: recibe request y devuelve response
services.py: lógica de negocio del módulo
validators.py: validaciones de entrada
constants.py: estados, nombres fijos, tipos

****************************************************************************************************
Fase 1: contrato funcional
Debes listar por cada pantalla del frontend:

URL o vista, método HTTP, parámetros de entrada, qué devuelve
fuente de datos
si modifica estado o solo consulta

Resultado esperado:
tener un inventario claro de endpoints.
****************************************************************************************************
Fase 2: modelo de datos del módulo
Debes definir:
 necesitan modelo Django

****************************************************************************************************
Fase 3: construir primero un flujo completo
No intentes hacer todo el módulo de una vez.
Empieza con un caso de uso completo.
Por ejemplo:

búsqueda por falla ID, obtención de datos del tablero
detalle de una escalación, listado filtrado
****************************************************************************************************
Fase 4: backend por capas
Por cada funcionalidad:

ruta en urls.py  --  entrada en views.py -- lógica en services.py 
si aplica:

ORM en models.py
Oracle en core/db/oracle
API en core/apis
****************************************************************************************************