## FUNCION PARA REALZIAR 
import calendar, time
from datetime import datetime
from dateutil.relativedelta import relativedelta
# MODEL DE DJANGO
from django.db.models import Q
# SERVICIOS
from app.service.PAG_func import get_pag_General, get_pag_MesActual
from app.service.reportes_sql import historico_de_indicadores
#MODELOS
from app.models.pag_reporte import PagReporte
from app.models import HiDeIndicadores


# Define qué páginas usan qué función
PAGINAS_CONFIG = {
    "pag_5": "actual",
    "pag_7": "actual",
    "pag_8": "5meses",
    "pag_9":  "actual",
    "pag_10": "5meses",
    "pag_11": "5meses",
    "pag_12": "5meses",
    "pag_13": "5meses",
    "pag_14": "actual",
    "pag_15": "5meses",
    "pag_16": "5meses",
    "pag_17": "actual",
    "pag_18": "actual",
    "pag_19": "5meses",
    "pag_20": "actual",
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

# REALIZA LA CREACION DE LOS NOMBRES DE LOS TEMPLATES Y PAG
def obtener_paginas_templates(id_empresa):
    # LISTA DEFAULT
    paginas_default = list(range(1, 21))
    # ==========================
    # VALIDAR ID EMPRESA
    if not id_empresa:
        paginas = paginas_default
        print("EMPRESA VACÍA → usando páginas por default")
    else:
        id_empresa = int(id_empresa)

        registro = PagReporte.objects.filter(
            id_cliente=id_empresa,
            estado=True
        ).first()
        # ==========================
        # VALIDAR RESULTADO
        if not registro:
            print("SIN REGISTRO → usando páginas por default")
            paginas = paginas_default
        elif isinstance(registro.paginas, list) and registro.paginas:
            paginas = registro.paginas
        else:
            print("REGISTRO SIN PÁGINAS VÁLIDAS → usando página 3")
            paginas = [3]
    # ==========================
    # FILTRAR (máximo hasta 10)
    paginas_filtradas = [p for p in paginas if p <= 21]
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

        # 🔹 NUEVO CAMPO
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
    ))
    #   VALIDAMOS SI YA TENEMOS LOS 6 MESES
    meses_db = {(d["mes"], d["ano"]) for d in data}

    meses_esperados = {
        (
            (fecha_base - relativedelta(months=i)).month,
            (fecha_base - relativedelta(months=i)).year
        )
        for i in range(6)
    }

    faltantes = meses_esperados - meses_db
    #   SI FALTAN MESES → CONSULTA E INSERTA
    if faltantes:
        cursor = conn.cursor()

        sql = historico_de_indicadores(datos) # 
        print(sql)
        cursor.execute(sql)
        columnas = [col[0] for col in cursor.description]
        resultados = [
            dict(zip(columnas, fila))
            for fila in cursor.fetchall()
        ]

        insertar_indicadores(resultados, datos)
        cursor.close()
        conn.close()
        #   RECONSULTAR YA CON DATOS INSERTADOS
        data = list(
            HiDeIndicadores.objects.filter(
                id_cliente=empresa,
                ano__gte=fecha_inicio.year,
                ano__lte=fecha_base.year
            ).values()
        )
    #   ORDEN FINAL (seguro)
    data.sort(key=lambda x: (x["ano"], x["mes"]))

    return data

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
