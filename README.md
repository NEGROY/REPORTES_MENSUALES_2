# REPORTES_MENSUALES_2
Reportes mensuales de CNOC 

Reportes automaticos, GENERACION AUTOMATICA DE REPORTES MENSUALES 

# SOLICITUDES DE MARLON:
- Catalogo_clientes, cada cliente tiene su where diferente deve guardarse por cliente, y se deve guardar el historial del where
- Formularios front end
- Formularios  catalogo cliente Create
- Formularios  catalogo cliente  Edit
- Formulario para crear reporte, pais, cliente, mes, sitios monitoreados "deve guardar log aque hora inicia proceso inicio de reporte"  y  Cuando termine que ya gener pdf
- maquetar reporte las 21 hojas que lleva el reporte mensual
- reporte debe ser configurable para cada cliente, en algunos cliente se quitan hojas pero los calculos son los mismos, asociar con el id   cliente
- consulta de base --> marlon soyos
- tomar de ejemplo las consultas realizadas en reporte automatizacion v1
- insert hoja 3

# --------------------------------- 06/03/2026 ---------------------------------
## Estructura
    /* AGREGAR esructura PRINCIPAL  */
reporte_cnoc/
│
├── app/
│   │
│   ├── main.py                # Punto de inicio FastAPI
│   │
│   ├── config/
│   │   └── database.py        # Conexión Oracle
│   │
│   ├── controllers/           # Controladores
│   │   ├── cliente_controller.py
│   │   ├── reporte_controller.py
│   │
│   ├── models/                # Modelos DB
│   │   ├── cliente_model.py
│   │   ├── reporte_model.py
│   │
│   ├── services/              # Lógica del negocio
│   │   ├── cliente_service.py
│   │   ├── reporte_service.py
│   │   └── pdf_service.py
│   │
│   ├── repositories/          # Acceso a datos
│   │   ├── cliente_repository.py
│   │   └── reporte_repository.py
│   │
│   ├── utils/
│   │   ├── logger.py
│   │   └── fechas.py
│   │
│   ├── templates/             # HTML
│   │   ├── clientes/
│   │   │   ├── create.html
│   │   │   └── edit.html
│   │   │
│   │   ├── reportes/
│   │   │   └── crear_reporte.html
│   │   │
│   │   └── layout.html
│   │
│   ├── static/
│   │   ├── css
│   │   ├── js
│   │   └── charts
│   │
│   └── reports/
│       └── templates_pdf/     # 21 hojas del reporte
│
│
├── docs/
│   └── consultas_sql/
│
├── tests/
│
├── requirements.txt
├── README.md
└── run.py

# REQUIAREMENTES 
- Python
- FastAPI
- Oracle DB
- Bootstrap
- Chart.js
- ReportLab

## Instalación
* Clonar proyecto                  
* git clone repo                   
* Instalar dependencias            
* pip install -r requirements.txt  
---

## Ejecutar proyecto
uvicorn app.main:app --reload
---

## 1 MIGRACIONES 
## 2 MODULO DE USUARIOS DE DJANGO 
## 3 (login)
## TOKEN CRFS


***EMPEZAR A REALIZAZR TODO 10/03/2026***
λ python --version
Python 3.13.0
λ pip --version
pip 25.3 from C:\laragon\bin\python\python-3.13\Lib\site-packages\pip (python 3.13)

*SE CREO EL PROYECTO*
venv\Scripts\activate
python -m django startproject config .

*Instalar driver MySQL para Django*
[X] pip install mysqlclient
[X] pip install PyMySQL
[X] -- CREA BASE DE DATOS EN LOCAL -- bd_mensual_cnoc
[X] python manage.py migrate

*CREAMO UN USUARIO*
[X] python manage.py createsuperuser
    nery.diaz - Cnoc2026

**CORRER EL SERVICIO**
python manage.py runserver

*CREAMOS MODELO DE DJANGO*
 {{Django solo genera migraciones dentro de una APP registrada, no dentro de cualquier carpeta.}}
 {{python manage.py sqlmigrate app 0001 || para ver qué cambios hará Django en la base de datos }}

*COMANDOS PARA LAS MIGRACIO0NES*
[ ] python manage.py makemigrations
[ ] python manage.py migrate

**MAS ADELANTE**
    {{pip install python-dotenv}}   # Cargar variables del .env
    {{pip install oracledb}}        # Driver de Oracle para Python


***ESTRUCTURA GENERAL PAGINAS***
VIEW
 │
 │ 1 prepara datos
 ▼
datosp5 = {
   date_ini
   date_end
   where_tk
   pais
}
 │
 ▼
SERVICE
get_pag5(datosp5)
 │
 ▼
SQL
ticktes(...)
 │
 ▼
resultado → template


 python manage.py runserver 172.20.97.137:5002

http://172.20.97.137:8000/menu/GT/



 cd C:\laragon\www\REPORTES_MENSUALES_2
 python manage.py runserver 172.20.97.137:8000


COMANDO PARA PROBAR LA CONECTIVIDAD DEL ORACLE 
  python manage.py test_oracle

# ORACLE_USER=
# ORACLE_PASSWORD= 
# ORACLE_DSN=172.17.114.223/sm9

# ORACLE_CLIENT_LIB=C:\oracle\instantclient_21_12
# ORACLE_CLIENT_LIB=C:\oracle\instantclient_23_9
# ORACLE_POOL_MIN=1
# ORACLE_POOL_MAX=5
# ORACLE_POOL_INC=1
# ORACLE_STMT_CACHE_SIZE=40
# ORACLE_FETCH_BATCH_SIZE=1000
# ORACLE_CALL_TIMEOUT_MS=60000


/* ESTRUCTUIRA PARA UTILIZAR FECTH  MANDAREMOS A LA BABY AJAX JQUERY (tendra vulnerabilidades ) */
fetch solo sirve para:
comunicar frontend ↔ backend

Frontend (JS)
   ↓
fetch / AJAX
   ↓
Django view (controlador)
   ↓
service.py (lógica y cálculos)
   ↓
models / API / Oracle
   ↓
JsonResponse


/* CORE | CNOC_APP | DESCRIPCION DE FUNCIONES  */
core/     → integraciones externas, APIs, Oracle, infraestructura
cnoc_app/ → templates, static, JS base, portal visual

/* ****  **** */