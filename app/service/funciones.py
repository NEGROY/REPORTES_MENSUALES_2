## FUNCION PARA REALZIAR 
import calendar
from datetime import datetime

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

## INDICE DE PAISES 
# TIKCKTE SNOMBRE NCOMPLETO  # PARQUE VA ABREVIADO
