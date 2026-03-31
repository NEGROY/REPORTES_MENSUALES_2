## FUNCION PARA REALZIAR 
import calendar, time
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db import transaction
# MODEL DE DJANGO
from django.db.models import Q
from collections import defaultdict
from django.core.paginator import Paginator

# SERVICIOS
from app.service.PAG_func import get_pag_General, get_pag_MesActual
from app.service.reportes_sql import historico_de_indicadores, Comportamiento
#MODELOS
from app.models.pag_reporte import PagReporte
from app.models import HiDeIndicadores, ParqueCnoc


# Define qué páginas usan qué función
PAGINAS_CONFIG = {
    "pag_5":  "actual",
    "pag_7":  "actual",
    "pag_8":  "actual",
    "pag_9":  "actual",
    "pag_10": "5meses",
    "pag_11": "5meses",
    "pag_12": "5meses",
    "pag_13": "5meses",
    "pag_14": "5meses",
    "pag_15": "actual",
    "pag_16": "5meses",
    "pag_17": "5meses",
    "pag_18": "actual",
    "pag_19": "actual",
    "pag_20": "5meses",
    "pag_21": "actual",
    "pag_22": "5meses",
    "pag_23": "5meses",
}
#DEFINIMOS LOS MESES 
meses_nombre = {
    "01": "ENERO",
    "02": "FEBRERO",
    "03": "MARZO",
    "04": "ABRIL",
    "05": "MAYO",
    "06": "JUNIO",
    "07": "JULIO",
    "08": "AGOSTO",
    "09": "SEPTIEMBRE",
    "10": "OCTUBRE",
    "11": "NOVIEMBRE",
    "12": "DICIEMBRE"
}
# SABEMOS QUE QUITAR _ / POR ESPACIOS 
CAMPOS_NORMALIZAR = {
    "pag_17": ["CODIGO DE CIERRE"],
    "pag_19": ["UBICACION"]
}

# REALIZA LA CREACION DE LOS NOMBRES DE LOS TEMPLATES Y PAG
def obtener_paginas_templates(id_empresa):
    # LISTA DEFAULT
    paginas_default = list(range(1, 22))
    # print( "paginas por def ", paginas_default)
    # ==========================
    # VALIDAR ID EMPRESA
    if not id_empresa:
        paginas = paginas_default
        print("EMPRESA VACÍA → usando páginas por default")
    else:
        id_empresa = int(id_empresa) # print( "EMPRESA ID" , id_empresa)

        registro = PagReporte.objects.filter(
            id_cliente=id_empresa,
            estado=1
        ).first()
        # ==========================
        # VALIDAR RESULTADO
        if not registro:
            print("SIN REGISTRO → usando páginas por default")
            paginas = paginas_default
        elif isinstance(registro.paginas, list) and registro.paginas:
            paginas = registro.paginas # print("PAGINAS ", paginas)
        else:
            print("REGISTRO SIN PÁGINAS VÁLIDAS → usando página 3")
            paginas = [3]
    # ==========================
    # FILTRAR (máximo hasta 10)
    # print( "paginas: ", paginas)
    paginas_filtradas = [p for p in paginas if p <= 30]
    # print( "paginas_filtradas: ", paginas_filtradas)
    # ==========================
    # TEMPLATES
    paginas_templates = [
        f"paginas/pag{p}.html"
        for p in paginas_filtradas
    ]
    # ==========================
    # NOMBRES PARA LÓGICA pag_1, pag2....
    paginas_nombres = [
        f"pag_{p}"
        for p in paginas_filtradas
    ]

    return {
        "templates": paginas_templates,
        "nombres": paginas_nombres
    }

# FUNCION PARA OBTENER TODOS LOS DATOS DE LAS PAGINAS
def generar_paginas_data(paginas_nombres, PAGINAS_CONFIG, datosPag, cadena_mes):
    # PAGINAS 
    paginas_data = {}

    for nombre_pag in paginas_nombres:
        # Validar configuración de la página
        tipo = PAGINAS_CONFIG.get(nombre_pag)
        if not tipo:
            # Ej: páginas sin query (pag_1, pag_2, etc.)
            continue
        try:
            print(f" EJECUTANDO CONSULTA: {nombre_pag}... {tipo}")
            time.sleep(0.5)  # medio segundo entre queries
            if tipo == "actual":
                resultado = get_pag_MesActual(datosPag, nombre_pag)
            elif tipo == "5meses":
                resultado = get_pag_General(datosPag, cadena_mes, nombre_pag)
            else:
                print(f" Tipo no reconocido en {nombre_pag}")
                resultado = None
            
            resultado = normalizar_dinamico(resultado)
            paginas_data[nombre_pag] = resultado

            # INTENTAMOS ELIMINAR _ / EN LAS PAG 
            if nombre_pag in CAMPOS_NORMALIZAR:
                resultado = limpiar_filas_con_headers(resultado, nombre_pag)
            # INTENTAMOS ELIMINAR _ / EN LAS PAG 
            
            print(f"✅ Finalizó {nombre_pag}")

        except Exception as e:
            print(f"❌ Error en {nombre_pag}: {e}")
            paginas_data[nombre_pag] = None  # evita que rompa todo

    return paginas_data
     
# FUNCIONCION PARA NORMALIZAR TODO 
def normalizar_dinamico(data):
    if not data:
        return {"headers": [], "rows": []}

    # detectar headers dinámicamente
    headers = list(data[0].keys())

    rows = []
    for fila in data:
        rows.append([fila.get(h, "") for h in headers])

    return {
        "headers": headers,
        "rows": rows
    }

## FUNCION PARA REALIZAR LOS CALCULOS DE LOS ULTMOS 6 MEESE
def ultimos_6_meses(mes, anio):

    meses_es = [
        "ENE","FEB","MAR","ABR","MAY","JUN",
        "JUL","AGO","SEP","OCT","NOV","DIC"
    ]

    data = {}

    for i in range(6):
        m = mes - i
        y = anio

        if m <= 0:
            m += 12
            y -= 1

        mes_num = f"{m:02d}"
        ultimo_dia = calendar.monthrange(y, m)[1]
        # HORAS POR MES
        horas_mes = ultimo_dia * 24

        fecha_ini = f"01{mes_num}{y}"
        fecha_fin = f"{ultimo_dia:02d}{mes_num}{y}"
        nombre_mes = f"{meses_es[m-1]}-{str(y)[2:]}"
        suf = "" if i == 0 else f"_{i}"

        data[f"MESN{suf}"] = mes_num
        data[f"MES{suf}"] = nombre_mes
        data[f"FECHA_INI{suf}"] = fecha_ini
        data[f"FECHA_FIN{suf}"] = fecha_fin

        # paginas_data.pag_20 NUEVO CAMPO
        data[f"HRSxMES{suf}"] = horas_mes

    data["ANO_1"] = anio if mes > 5 else anio - 1
    data["ANO_2"] = anio

    # ENTRE CADA MES TAMBIEN OBTENER EL TOTAL DE LOS DIAS Y MULTIPLICAR POR 24 PARA QUE DEVUELVA EL TOTAL DE HRSxMES

    return data

# FUNCION PARA TRAER DATOS HISTORICOS
def obtener_historico_indicadores(conn, datos):
    # DATOS DE CONSULTA 
    mes  = int(datos["mes"])
    anio = int(datos["anio"])
    empresa = datos["empresa"]    
    #   Fecha base
    fecha_base = datetime(anio, mes, 1)
    #   RANGO (más eficiente que lista + Q manual)
    fecha_inicio = fecha_base - relativedelta(months=5)
    #   Consulta directa (SIN exists)
    query = HiDeIndicadores.objects.filter(
         id_cliente=empresa,
         ano__gte=fecha_inicio.year,
         ano__lte=fecha_base.year
     )
    
    data = list(query.values(
         "mes", "ano",
         "inci_menor_o_8", "inci_mayor_a_8",
         "productividad", "sitios_reincidentes",
         "indice_de_reincidencia", "mttr_promedio", 
         "disponibilidad", "proactividad"
     ))   # > print(data, "DATOS DEL MES ACTUAL")
     
    #   VALIDAMOS SI YA TENEMOS LOS 6 MESES
    meses_db = {(d["mes"], d["ano"]) for d in data}
    # -----------------
    meses_esperados = {
        (
            (fecha_base - relativedelta(months=i)).month,
            (fecha_base - relativedelta(months=i)).year
        )
        for i in range(6)
    }
    faltantes = meses_esperados - meses_db # print("meses_esperados:",meses_esperados, "MESE DB:", meses_db)
    #   SI FALTAN MESES → CONSULTA E INSERTA
    if faltantes:
        cursor = conn.cursor()

        sql = historico_de_indicadores(datos) # print(sql)
        cursor.execute(sql)
        columnas = [col[0] for col in cursor.description]
        resultados = [
            dict(zip(columnas, fila))
            for fila in cursor.fetchall()
        ]

        insertar_indicadores(resultados, datos) # print( "insertar_indicadores: ")
        cursor.close()
        conn.close()
        #   RECONSULTAR YA CON DATOS INSERTADOS
                    
    data = list(
    HiDeIndicadores.objects.filter(
        id_cliente=empresa
    ).filter(
        Q(ano=fecha_inicio.year, mes__gte=fecha_inicio.month) |
        Q(ano=fecha_base.year,  mes__lte=fecha_base.month) |
        Q(ano__gt=fecha_inicio.year, ano__lt=fecha_base.year)
    ).values( "mes", "ano",
        "inci_menor_o_8", "inci_mayor_a_8",
        "productividad", "sitios_reincidentes",
        "indice_de_reincidencia", "mttr_promedio", 
        "disponibilidad", "proactividad")
    )
    #   ORDEN FINAL (seguro)
    data.sort(key=lambda x: (x["ano"], x["mes"]))

    return data

#  OBTENEMOS DATOS Comportamiento de la Red del Cliente || ParqueCnoc
def Comporta8(conn, datos):
    mes     = int(datos["mes"])
    anio    = int(datos["anio"])
    empresa = datos["empresa"]
    sitios_activos = datos["total_enlaces"]

    fecha_base   = datetime(anio, mes, 1)
    fecha_inicio = fecha_base - relativedelta(months=5)
    
    # ===============================
    # 1. ASEGURAR EXISTENCIA DEL MES
    # ===============================
    actual = ParqueCnoc.objects.filter(
        id_cliente_id=empresa,
        mes=mes,
        ano=anio
    ).first()

    if not actual:
        try:
            # ---- Intentar comportamiento ----
            datos_sql = datos.copy()
            datos_sql["date_ini"] = fecha_base.strftime("%Y-%m-01")
            datos_sql["date_end"] = fecha_base.strftime("%Y-%m-31")

            sql = Comportamiento(datos_sql)

            with conn.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()

            data = {
                "Total de Enlaces de datos": 0,
                "Internet": 0,
                "AE": 0,
                "Total de TT": 0
            }

            for tipo, total, _ in rows:
                data[tipo] = total

            with transaction.atomic():
                ParqueCnoc.objects.create(
                    id_cliente_id=empresa,
                    mes=mes,
                    ano=anio,
                    tt_EnlacesDatos= data["tt_EnlacesDatos"],
                    internet=data["Internet"],
                    AE=data["AE"],
                    tt_tt=data["Total de TT"],
                    sitios_activos = sitios_activos
                )

        except Exception:
            # ---- Fallback: copiar último mes ----
            ultimo = (
                ParqueCnoc.objects
                .filter(id_cliente_id=empresa)
                .order_by("-ano", "-mes")
                .first()
            )

            if ultimo:
                with transaction.atomic():
                    ParqueCnoc.objects.create(
                        id_cliente_id=empresa,
                        mes=mes,
                        ano=anio,
                        sitios_activos= sitios_activos,
                        tt_EnlacesDatos=ultimo.tt_EnlacesDatos,
                        internet=ultimo.internet,
                        AE=ultimo.AE,
                        tt_tt=ultimo.tt_tt
                    )
    # ===============================
    # 2. RECONSULTA FINAL (OPTIMIZADA)
    # ===============================
    data = list(
        ParqueCnoc.objects.filter( id_cliente_id=empresa ).filter(
        Q(ano=fecha_inicio.year, mes__gte=fecha_inicio.month) |
        Q(ano=fecha_base.year,  mes__lte=fecha_base.month)
        ).values(
            "sitios_activos",
            "tt_EnlacesDatos",
            "internet",
            "AE",
            "tt_tt",
            "id_cliente_id",
            "mes",
            "ano",
        )
    )
    # ORDEN FINAL SEGURO (por si MySQL/MariaDB se pone creativo)
    data.sort(key=lambda x: (x["ano"], x["mes"]))

    return data

# Función auxiliar para limpiar filas según headers
def limpiar_filas_con_headers(resultado, nombre_pag):
    if not resultado:
        return resultado

    headers = resultado.get("headers", [])
    rows = resultado.get("rows", [])

    campos = CAMPOS_NORMALIZAR.get(nombre_pag, [])
    if not campos:
        return resultado

    # Mapear índices de columnas a normalizar
    idxs = [headers.index(c) for c in campos if c in headers]

    filas_limpias = []
    for fila in rows:
        fila = list(fila)
        for idx in idxs:
            fila[idx] = normalizar_campo(fila[idx])
        filas_limpias.append(tuple(fila))

    resultado["rows"] = filas_limpias
    return resultado
# Función de normalización de texto PARA LA DE ARRIBA 
def normalizar_campo(valor):
    if valor is None:
        return None
    return (
        str(valor)
        .replace("_", " ")
        .replace("/", " ")
        .strip()
    )

# FUNCION PARA INSERTAR DATOS DE INDICADORES DESDE EL MODELO 
def insertar_indicadores(data, empresa):
    objetos = []

    empresa_id = empresa.get("empresa")
    mes = empresa.get("mes")
    ano = empresa.get("anio")
    #   Traer existentes (evita duplicados)
    existentes = set(
        HiDeIndicadores.objects.filter(id_cliente_id=empresa_id)
        .values_list('mes', 'ano')
    )
    for item in data:
        clave = (mes, ano)
        if clave not in existentes:
            objetos.append(
                HiDeIndicadores(
                    id_cliente_id=empresa_id,  #   FIX FK
                    mes=mes,
                    ano=ano,
                    #   MAPEO DESDE TU DATA || los valores vacios estna default 0 en la BD 
                    inci_menor_o_8=item.get('INDICE_MENOR_8'),
                    inci_mayor_a_8=item.get('INDICE_MAYOR_8'),
                    productividad=item.get('PROACTIVIDAD'),
                    sitios_reincidentes=item.get('SITIOS_REINCIDENTES'),
                    indice_de_reincidencia=item.get('INDICE_REINCIDENCIA'),
                    mttr_promedio=item.get('MTR'),
                        #   CAMPOS EXTRA (si luego los usas)
                    disponibilidad=0,
                )
            )
    #   INSERT MASIVO
    if objetos:
        HiDeIndicadores.objects.bulk_create(objetos, ignore_conflicts=True)

## INDICE DE PAISES 
# TIKCKTE SNOMBRE NCOMPLETO  # PARQUE VA ABREVIADO

# PARA LAS PAGINACION DE DISPONIBILIDAD DE LA PAG 21 
def paginacion(data, por_pagina=30):
    headers = data['headers']
    rows = data['rows']

    # paginas_data.pag_20 Orden fijo de países
    orden_paises = [
        'GUATEMALA',
        'EL SALVADOR',
        'HONDURAS',
        'COSTA RICA',
        'NICARAGUA'
    ]

    # paginas_data.pag_21 Agrupar por país
    agrupado = defaultdict(list)
    for row in rows:
        agrupado[row[4]].append(row)

    paginas = []
    # paginas_data.pag_21 PAGINAR PAÍS POR PAÍS (ESTA ES LA CLAVE)
    for pais in orden_paises:
        if pais not in agrupado:
            continue
    # Orden interno por disponibilidad
        filas_ordenadas = sorted(
            agrupado[pais],
            key=lambda x: x[3],
            reverse=True
        )

        paginator = Paginator(filas_ordenadas, por_pagina)

        for num in paginator.page_range:
            pagina = paginator.page(num)

            paginas.append({
                "pais": pais,
                "pagina": pagina
            })

    return {
        "headers": headers,
        "paginas": paginas,
        "total_paginas": len(paginas)
    }

#paginacion de las ocho horas 
def paginacion8 (rows, filas_por_pagina=35):
 
    paginas = []
    for i in range(0, len(rows), filas_por_pagina):
        paginas.append(rows[i:i + filas_por_pagina])
    return paginas

# FUNCION QUE VALIDA CAMPOS Y AGREGAR 0 Y TOTAL 
def validaROWS10(pagina, requeridos):
    """
    Valida la estructura de pag_10:
    - Verifica existencia de MONITOREO REACTIVO y PROACTIVO
    - Crea filas faltantes con ceros
    - Recalcula y agrega fila TOTAL al final
    """

    headers = pagina.get("headers", [])
    rows = pagina.get("rows", [])

    # Validación mínima de estructura
    if not headers or len(headers) <= 1:
        return pagina

    total_cols = len(headers) - 1
    # -----------------------------
    # Tipos de monitoreo requeridos
    # -----------------------------
    requeridos = requeridos

    existentes = {row[0] for row in rows if row}
    # -----------------------------
    # 2️⃣ Crear filas faltantes
    # -----------------------------
    for nombre in requeridos:
        if nombre not in existentes:
            rows.append([nombre] + [0] * total_cols)

    # -----------------------------
    # 3️⃣ Eliminar TOTAL previo (si existe)
    # -----------------------------
    rows[:] = [row for row in rows if row[0] != "TOTAL"]

    # -----------------------------
    # 4️⃣ Calcular TOTAL
    # -----------------------------
    fila_total = ["TOTAL"]

    for col in range(1, total_cols + 1):
        suma = sum(
            (row[col] or 0)
            for row in rows
            if len(row) > col
        )
        fila_total.append(suma)

    # -----------------------------
    # 5️⃣ Agregar fila TOTAL
    # -----------------------------
    rows.append(fila_total)

    return pagina