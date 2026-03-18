
# CONSULTA BASE POR LO BENERAL  LA QUE VIENE DE PRIMERO 
def sql_base(date_ini='01012026', date_end='31012026', where_tk=" probsummarym1.company LIKE '%BANCO DE DESARROLLO RURAL%' ",pais='CENAM', paiscomplete= 'GUATEMALA'):
    
    # IF SI PAIS SE = CENAM NO PONER WHERE PAIS, SI ES LO CONTRARIO PONER EL PAIS
    filtro_pais = ""
    if pais != 'CENAM':
       filtro_pais = f" WHERE TK.PAIS = '{paiscomplete}' "
    
    query =f""" with
        VARIABLES AS (
            SELECT 1 COD,
            TO_DATE('{date_ini}','DDMMYYYY') F_INI,
            TO_DATE('{date_end}','DDMMYYYY') F_FIN,
            '{paiscomplete}' PAIS
            FROM DUAL
            ),
        tickets_enlaces as ( 
            select probsummarym1."NUMBER", tg_enlace, (
                case 
                    when ( ( probsummarym2.tg_enlace is null
                            or probsummarym2.tg_enlace = '0'
                            or probsummarym2.tg_enlace = 'C' )
                           and probsummarym1.brief_description like '%"%'
                           and length(probsummarym1.brief_description) <= 25 ) then
                           replace( 
                              probsummarym1.brief_description,
                              '"'
                            )
                        else 
                        probsummarym2.tg_enlace
                     end
                  ) enlace, tg_enlace_destino, tg_company_cnoc, company,
                  ( case
                        when ( probsummarym1.company is not null
                           and probsummarym1.company not like '%DEFAULT%' ) then
                           probsummarym1.company
                        when ( probsummarym1.company is not null
                           and probsummarym1.company like '%DEFAULT%' ) then
                           (
                              case
                                 when ( probsummarym2.tg_company_cnoc is not null
                                    and probsummarym2.tg_company_cnoc not like '%DEFAULT%' ) then
                                    probsummarym2.tg_company_cnoc
                                 when ( probsummarym2.tg_company_cnoc is not null
                                    and probsummarym2.tg_company_cnoc like '%DEFAULT%' ) then
                                    probsummarym1.company
                                 when ( probsummarym2.tg_company_cnoc is null ) then
                                    probsummarym1.company
                              end
                           )
                        when ( probsummarym1.company is null
                           and probsummarym2.tg_company_cnoc is not null
                           and probsummarym2.tg_company_cnoc not like '%DEFAULT%' ) then
                           probsummarym2.tg_company_cnoc
                        else
                           '-----'
                     end
                  ) cliente,
                  brief_description,
                  probsummarym1.close_time,
                  probsummarym1.open_time,
                  probsummarym1.category,
                  probsummarym1.action,
                  probsummarym1.subcategory,
                  probsummarym1.product_type,
                  probsummarym2.res_anal_code,
                  probsummarym1.problem_type,
                  probsummarym1.resolved_group,
                  probsummarym1.opened_by,
                  ( probsummarym1.close_time - probsummarym1.open_time ) * 24 as "T VIDA TICKET (horas)",
                  (
                     select sum(to_date(to_char(
                        total,
                        'DD/MM/YYYY HH24:MI:SS'
                     ),
                       'DD/MM/YYYY HH24:MI:SS') - to_date('01/01/4000 00:00:00',
                   'DD/MM/YYYY HH24:MI:SS')) * 24 as "Pending Customer"
                       from clocksm1
                      where probsummarym1."NUMBER" = clocksm1.key_char
                        and name = 'Pending Customer'
                      group by key_char
                  ) as "Pending Customer (horas)",
                  (
                     select sum(to_date(to_char(
                        total,
                        'DD/MM/YYYY HH24:MI:SS'
                     ),
                       'DD/MM/YYYY HH24:MI:SS') - to_date('01/01/4000 00:00:00',
                   'DD/MM/YYYY HH24:MI:SS')) * 24 as "WO Pending Customer"
                       from clocksm1
                      where probsummarym1."NUMBER" = clocksm1.key_char
                        and name like '%WO Pending Customer%'
                      group by key_char
                  ) as "WO Pending Customer (horas)",
                  (
                     select sum(to_date(to_char(
                        total,
                        'DD/MM/YYYY HH24:MI:SS'
                     ),
                       'DD/MM/YYYY HH24:MI:SS') - to_date('01/01/4000 00:00:00',
                   'DD/MM/YYYY HH24:MI:SS')) * 24 as "Resolved"
                    from clocksm1
                      where probsummarym1."NUMBER" = clocksm1.key_char
                        and name like '%Resolved%'
                      group by key_char
                  ) as "Resolved (horas)",
                  (
                     select sum(to_date(to_char(
                        total,
                        'DD/MM/YYYY HH24:MI:SS'
                     ),
                       'DD/MM/YYYY HH24:MI:SS') - to_date('01/01/4000 00:00:00',
                   'DD/MM/YYYY HH24:MI:SS')) * 24 as "Monitoreo"
                       from clocksm1
                      where probsummarym1."NUMBER" = clocksm1.key_char
                        and name like '%Monitoreo%' group by key_char
                  ) as "Monitoreo (horas)",
                  (
                     select sum(to_date(to_char(
                        total,
                        'DD/MM/YYYY HH24:MI:SS'
                     ),
                       'DD/MM/YYYY HH24:MI:SS') - to_date('01/01/4000 00:00:00',
                   'DD/MM/YYYY HH24:MI:SS')) * 24 as "Dictamen"
                       from clocksm1
                      where probsummarym1."NUMBER" = clocksm1.key_char
                        and name like '%Dictamen%'
                      group by key_char
                  ) as "Dictamen (horas)"
             from probsummarym1,
                  probsummarym2
            where probsummarym1."NUMBER" = probsummarym2."NUMBER"
            AND  (
            -- WHERE A MODIFIVAR
          {where_tk}
          )
          -- WHERE
              and probsummarym1.assignment in ( 'CNOC','CNOC_CBO_PROACTIVO','CNOC_CBO_REACTIVO','CNOC_MASIVO',
                                                'GESTION DE DATOS N1','GESTION N1_CBO','GT - ACC. EMPRESARIAL - NOC',
                                                'SOPORTE_N1_XT','SOPORTE_N2_XT' )
              and ( probsummarym1.resolved_group in ( 'CNOC','CNOC_CBO_PROACTIVO','CNOC_CBO_REACTIVO',
                                                      'CNOC_MASIVO','GESTION DE DATOS N1','GESTION N1_CBO',
                                                      'GT - ACC. EMPRESARIAL - NOC','SOPORTE_N1_XT','SOPORTE_N2_XT' )
               or probsummarym1.resolved_group is null )
              and ( probsummarym1.close_time between (
              select F_INI
                from variables
           ) and (
              select  (F_FIN + 1) 
                from variables
           ) 
        ) 
        ),tk as (
           select a.*,
                  case
                     when tt_resta > "T VIDA TICKET (horas)" then
                        tt_resta - "T VIDA TICKET (horas)"
                     else
                        "T VIDA TICKET (horas)" - tt_resta
                  end "T TICKET ACTIVO (horas)"
             from (
              select tk."NUMBER" ticket, tk.enlace, tk.tg_enlace_destino ubicacion,
                     case
                        when regexp_substr( tk.enlace, '_GT_', 1, 1, 'i' ) = '_GT_'
                            or enlace like '%T' or enlace like '%GUATEMALA%' then 'GUATEMALA'
                        when regexp_substr( tk.enlace, '_SV_', 1, 1, 'i' ) = '_SV_'
                            or enlace like '%SV' or enlace like '%SALVADOR%' then 'EL SALVADOR'
                        when regexp_substr( tk.enlace, '_CR_', 1, 1, 'i' ) = '_CR_'
                            or enlace like '%OC' or enlace like '%COSTA RICA%' then 'COSTA RICA'
                        when regexp_substr(tk.enlace, '_NI_', 1, 1, 'i') = '_NI_'
                            or enlace like '%ON' or enlace like '%NICARAGUA%' then 'NICARAGUA'
                        when regexp_substr( tk.enlace, '_HN_', 1, 1,'i') = '_HN_'
                            or enlace like '%OH' or enlace like '%HONDURAS%' then 'HONDURAS'
                        when ( tk.enlace like 'FG%' or tk.enlace like '%FEMTO_GT%' ) then 'FEMTOCELDA GUATEMALA'
                        when ( tk.enlace like 'FS%' or tk.enlace like '%FEMTO_SV%' ) then 'FEMTOCELDA EL SALVADOR'
                        when ( tk.enlace like 'FH%' or tk.enlace like '%FEMTO_HN%' ) then 'FEMTOCELDA HONDURAS'
                        when ( tk.enlace like '%FEMTO_NI%' ) then 'FEMTOCELDA NICARAGUA'
                        when ( tk.enlace like 'F%' ) then 'FEMTOCELDA'
                        else
                           (
                              case
                                 when device2m1.tg_country_code = 'GT' then 'GUATEMALA'
                                 when device2m1.tg_country_code = 'SV' then 'EL SALVADOR'
                                 when device2m1.tg_country_code = 'CR' then 'COSTA RICA'
                                 when device2m1.tg_country_code = 'NI' then 'NICARAGUA'
                                 when device2m1.tg_country_code = 'HN' then 'HONDURAS'
                                 when device2m1.tg_country_code = 'PA' then 'PANAMA'
                                 else
                                    null
                              end
                           )
                     end pais,
                     to_char(
                        tk.close_time,
                        'MM'
                     ) "MES CIERRE",
                     tk.tg_company_cnoc,
                     tk.cliente,
                     tk.brief_description "PROBLEMA REPORTADO",
                     tk.action "DETALLE PROBLEMA REPORTADO",
                     tk.category falla,
                     tk.subcategory subfalla,
                     tk.product_type "SUB SUBFALLA",
                     (
                        case
                           when tk.category = 'DX - BOLETA MAL ABIERTA' and tk.opened_by = 'tmipuser' then 'CLARO'
                           when tk.res_anal_code = 'CALL CENTER' or tk.res_anal_code = 'TEMIP' then 'CLARO'
                           when ( tk.category = 'DX - CLIENTE'
                               or tk.category = 'DX - BOLETA MAL ABIERTA'
                               or tk.category = 'DX - SIN INTERVENCION TECNICA'
                               or tk.subcategory = 'CLIENTE' ) then
                              'CLIENTE'
                           else
                              'CLARO'
                        end
                     ) "ATRIBUIBLE A",
                     tk."T VIDA TICKET (horas)",
                     ( coalesce( "Pending Customer (horas)", 0 ) 
                     + coalesce( "WO Pending Customer (horas)", 0 ) 
                     + coalesce( "Resolved (horas)", 0 ) 
                     + coalesce( "Monitoreo (horas)", 0 ) 
                     + coalesce( "Dictamen (horas)", 0 ) ) 
                     tt_resta, tk.close_time "FECHA DE CIERRE",
                     tk.open_time "FECHA DE APERTURA", tk.res_anal_code "CODIGO DE CIERRE",
                     tk.problem_type, tg_id_clase_servicio servicio,
                     resolved_group "GRUPO QUE RESOLVIO",
                     case
                        when ( resolved_group = 'CNOC'
                            or resolved_group = 'CNOC_CBO_PROACTIVO'
                            or resolved_group = 'CNOC_MASIVO' )
                           and ( "OPENED_BY" = 'tmipuser' ) then
                           'MONITOREO PROACTIVO'
                        when ( resolved_group = 'CNOC_CBO_REACTIVO'
                            or resolved_group = 'GESTION DE DATOS N1'
                            or resolved_group = 'GESTION N1_CBO'
                            or resolved_group = 'GT - ACC. EMPRESARIAL - NOC'
                            or resolved_group like '%SOPORTE_N1_XT%'
                            or resolved_group like '%SOPORTE_N2_XT%' )
                           and ( "OPENED_BY" <> 'tmipuser' ) then
                           'MONITOREO REACTIVO'
                        else
                           'MONITOREO REACTIVO'
                     end "TIPO MONITOREO",
                     "OPENED_BY"
                from tickets_enlaces tk
                left join device2m1
              on device2m1.logical_name = tk.enlace
           ) a
        ),TICKETS_2 as (
           select tk.*,
                  case
                     when ( "T TICKET ACTIVO (horas)" >= 0 )
                        and ( "T TICKET ACTIVO (horas)" <= 0.5 ) then 'RANGO DE 0 A 0.5 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 0.5 )
                        and ( "T TICKET ACTIVO (horas)" <= 1 ) then 'RANGO DE 0.5 A 1 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 1 )
                        and ( "T TICKET ACTIVO (horas)" <= 2 ) then 'RANGO DE 1 A 2 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 2 )
                        and ( "T TICKET ACTIVO (horas)" <= 4 ) then 'RANGO DE 2 A 4 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 4 )
                        and ( "T TICKET ACTIVO (horas)" <= 8 ) then 'RANGO DE 4 A 8 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 8 )
                        and ( "T TICKET ACTIVO (horas)" <= 12 ) then 'RANGO DE 8 A 12 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 12 ) then  'RANGO MAS DE 12 HORAS'
                     else
                        'PRUEBAS'
                  end "RANGO SOLUCION",
                  case
                     when ( "T TICKET ACTIVO (horas)" >= 0 )
                        and ( "T TICKET ACTIVO (horas)" <= 8 ) then
                        'RANGO DE 0 A 8 HORAS'
                     when ( "T TICKET ACTIVO (horas)" > 8 ) then
                        'RANGO MAS DE 8 HORAS'
                     else
                        'PRUEBAS'
                  end "RANGO SOLUCION 2",
                  ( ( ( "FECHA DE CIERRE" ) - ( "FECHA DE APERTURA" ) ) * 24 ) as "DURACION TICKET (horas)"
             from tk
    {filtro_pais}
        ) ,
    """
    
    return query 
    # --  SELECT * FROM TICKETS_2

# CONSULTA PARA LOS Histórico de Indicadores (PAG 6) 
def historico_de_indicadores(parque_where=""" WHERE CLIENTE LIKE '%BANCO DE DESARROLLO RURAL%'  AND PAIS='GT' """):
    
    query = sql_base()+ f""" 
          -------------historico_de_indicadores-----------   
        TT_ENLACES AS (
            SELECT COUNT(*) FROM  FR_PARQUE_SERVICIOS_CENAM     
            {parque_where}
        ),
        -- FIN CONSULTA BAS
        --SELECT * FROM TICKETS_2;
        TK AS (SELECT * FROM TICKETS_2 ),
        TK_ATRIBUCION_CLIENTE AS (SELECT * FROM TICKETS_2 WHERE  "ATRIBUIBLE A"='CLIENTE'), 
        TK_PROACTIVOS AS (SELECT "TIPO MONITOREO" FROM TK)
        , RANGO_SOLUCION AS (
            SELECT
          --  *
            "RANGO SOLUCION 2"  R,COUNT(*) CONTAR 
            FROM TICKETS_2
                   GROUP BY "RANGO SOLUCION 2"  )
        --SELECT * FROM RANGO_SOLUCION;
            SELECT    NVL(R_MENOR_8,0) R_MENOR_8,
                NVL(R_MAYOR_8,0) R_MAYOR_8,
                CASE
                    WHEN R_MENOR_8=0 THEN 0
                ELSE
                    NVL(ROUND((R_MENOR_8 / TT_TK)*100,2),0)
                END INDICE_MENOR_8,
                CASE
                    WHEN R_MAYOR_8=0 THEN 0
                ELSE
                    NVL(ROUND((R_MAYOR_8 / TT_TK)*100,2),0) 
               END INDICE_MAYOR_8,
                CASE
                    WHEN PRO=0 THEN 0
                ELSE
                    NVL(ROUND((PRO/TT_TK) *100,2),0) END "PROACTIVIDAD",
                CASE
                    WHEN TT_TK_CLIENTE=0 THEN 0
                ELSE
                    NVL(ROUND(((TT_TK-TT_TK_CLIENTE)/TT_ENLACES)*100,2),0) END "INDICE DE FALLAS",
                 NVL(INDI,0) "SITIOS REINCIDENTES",
                CASE
                    WHEN INDI=0 THEN 0
                ELSE
                    NVL(ROUND( (INDI / TT_ENLACES)*100,2),0) END INDICE_REINCIDENCIA,
                    NVL(ROUND( PROMEDIO,2),0) MTR

               FROM (
        SELECT  
          NULLIF((SELECT CONTAR FROM RANGO_SOLUCION WHERE R='RANGO DE 0 A 8 HORAS'),0) R_MENOR_8,
            NULLIF((SELECT CONTAR FROM RANGO_SOLUCION WHERE R='RANGO MAS DE 8 HORAS'),0) R_MAYOR_8,
            NULLIF((SELECT COUNT(*) FROM TK),0) TT_TK,
            NULLIF((SELECT COUNT(*) FROM TK_ATRIBUCION_CLIENTE),0) TT_TK_CLIENTE,
            NULLIF(( SELECT * FROM TT_ENLACES),0) TT_ENLACES ,
            NULLIF((SELECT COUNT(*) FROM TK_PROACTIVOS WHERE "TIPO MONITOREO"='MONITOREO PROACTIVO'),0) PRO,
            NULLIF((SELECT avg("T TICKET ACTIVO (horas)") FROM TK
            -- AGREGAR WHERE SE TOME LA TODOS DEL MES QUE SE ESTA GENERANDO EL REPORTES 
             WHERE "FECHA DE APERTURA" BETWEEN 
               (SELECT F_INI FROM VARIABLES)
             AND (SELECT F_FIN FROM VARIABLES)
            --  *************************
            ),0) PROMEDIO,
            NULLIF((SELECT COUNT(ENLACE) ENLACE FROM (SELECT COUNT(ENLACE) ENLACE FROM TK  GROUP BY ENLACE HAVING COUNT(ENLACE)>=2)),0) INDI
    FROM DUAL)A  """

    return query


    #   probsummarym1.company LIKE '%BANCO DE DESARROLLO RURAL%'
    #     OR probsummarym2.TG_COMPANY_CNOC LIKE '%BANCO DE DESARROLLO RURAL%'
    #     OR probsummarym1.brief_description LIKE '%BANCO DE DESARROLLO RURAL%'
    #     OR probsummarym1.action LIKE '%BANCO DE DESARROLLO RURAL%'
    #     --OR tk.tg_enlace_destino LIKE '%BANCO DE DESARROLLO RURAL%'
    #     OR tg_enlace LIKE '%CC\\_BANRURAL\\_GT%' ESCAPE '\\'

## FUNCION QUE REALIZA LA CONVERSION SACA LOS ULTIMOS 6 MESES 
def map_fechas():
    SQL = """
WITH
VARIABLES AS (
SELECT A.*, :cod COD,
to_char(LAST_DAY(TO_DATE(FECHA_INI) ),'DDMMYYYY') FECHA_FIN,
to_char(LAST_DAY(TO_DATE(FECHA_INI_1) ),'DDMMYYYY') FECHA_FIN_1,
to_char(LAST_DAY(TO_DATE(FECHA_INI_2) ),'DDMMYYYY') FECHA_FIN_2,
to_char(LAST_DAY(TO_DATE(FECHA_INI_3) ),'DDMMYYYY') FECHA_FIN_3,
to_char(LAST_DAY(TO_DATE(FECHA_INI_4) ),'DDMMYYYY') FECHA_FIN_4,
to_char(LAST_DAY(TO_DATE(FECHA_INI_5) ),'DDMMYYYY') FECHA_FIN_5,
TO_CHAR(TO_DATE(FECHA_INI), 'MON-YY', 'NLS_DATE_LANGUAGE=SPANISH') MES,
TO_CHAR(TO_DATE(FECHA_INI_1), 'MON-YY', 'NLS_DATE_LANGUAGE=SPANISH') MES_1,
TO_CHAR(TO_DATE(FECHA_INI_2), 'MON-YY', 'NLS_DATE_LANGUAGE=SPANISH') MES_2,
TO_CHAR(TO_DATE(FECHA_INI_3), 'MON-YY', 'NLS_DATE_LANGUAGE=SPANISH') MES_3,
TO_CHAR(TO_DATE(FECHA_INI_4), 'MON-YY', 'NLS_DATE_LANGUAGE=SPANISH') MES_4,
TO_CHAR(TO_DATE(FECHA_INI_5), 'MON-YY', 'NLS_DATE_LANGUAGE=SPANISH') MES_5

FROM (
SELECT 
to_char(TRUNC(TO_DATE(FECHA_BUSCAR), 'MONTH'),'DDMMYYYY') FECHA_INI,
to_char(ADD_MONTHS(TO_DATE(FECHA_BUSCAR),-1),'DDMMYYYY') FECHA_INI_1,
to_char(ADD_MONTHS(TO_DATE(FECHA_BUSCAR),-2),'DDMMYYYY') FECHA_INI_2,
to_char(ADD_MONTHS(TO_DATE(FECHA_BUSCAR),-3),'DDMMYYYY') FECHA_INI_3,
to_char(ADD_MONTHS(TO_DATE(FECHA_BUSCAR),-4),'DDMMYYYY') FECHA_INI_4,
to_char(ADD_MONTHS(TO_DATE(FECHA_BUSCAR),-5),'DDMMYYYY') FECHA_INI_5
FROM (
SELECT 
TO_DATE(:fecha,'DDMMYYYY') FECHA_BUSCAR
FROM DUAL
) B
) A
)

SELECT 
TO_CHAR(TO_DATE(FECHA_INI), 'MM') MESN,
TO_CHAR(TO_DATE(FECHA_INI_1), 'MM') MESN_1,
TO_CHAR(TO_DATE(FECHA_INI_2), 'MM') MESN_2,
TO_CHAR(TO_DATE(FECHA_INI_3), 'MM') MESN_3,
TO_CHAR(TO_DATE(FECHA_INI_4), 'MM') MESN_4,
TO_CHAR(TO_DATE(FECHA_INI_5), 'MM') MESN_5,
MES,MES_1,MES_2,MES_3,MES_4,MES_5,
FECHA_INI,FECHA_FIN,FECHA_INI_1,FECHA_FIN_1,
FECHA_INI_2,FECHA_FIN_2,FECHA_INI_3,FECHA_FIN_3,
FECHA_INI_4,FECHA_FIN_4,FECHA_INI_5,FECHA_FIN_5
FROM VARIABLES
"""
    return SQL

## PRUEBAS DE HORAS  ELIMINAR 
def map_fechas_pruebas():
    SQL = """
SELECT 
    :fecha valor,
    TO_DATE(:fecha,'DDMMYYYY') fecha_convertida
FROM DUAL
"""
    return SQL


# ************************************************************
## PAGINA 5 Indicadores  || Resp. Incidentes %
def pag_5(date_ini,date_end, where_tk,pais, paiscomplete):
 
   #  CONSULTA COMPLETA  
   sql = sql_base(date_ini,date_end, where_tk, pais, paiscomplete) + f"""  a as ( select "ATRIBUIBLE A",COUNT(*) CONTAR from tk group by "ATRIBUIBLE A")
        , b as (
        SELECT
        CASE 
            WHEN "ATRIBUIBLE A" ='CLARO' THEN CONTAR
            ELSE 0
            END CLARO,
        CASE 
            WHEN "ATRIBUIBLE A" ='CLIENTE' THEN CONTAR
            ELSE 0
            END CLIENTE
         FROM a)
        , c as (
         SELECT  COLUMNA,VALOR
        FROM (
          SELECT CLARO, CLIENTE
          FROM b
        )
        UNPIVOT (
          VALOR FOR COLUMNA IN (CLARO, CLIENTE)
        )

        )
        SELECT COLUMNA,SUM(VALOR) VALOR,SUM("%") "PORCENTAJE",TT FROM (
        select c.*, round((VALOR/(SELECT SUM(CONTAR) FROM a))*100,2) "%",(SELECT SUM(CONTAR) FROM a)TT  from c
        )A GROUP BY COLUMNA,TT 
    """
   
   return sql

# ************************************************************
# PAGI 7 Comportamiento de la Red del Cliente
def pag_7(date_ini,date_end, where_tk,pais, paiscomplete ):

    # sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f"""
    # """

    return 

# ************************************************************
# PAGI 8 Distribución de Incidentes
def pag_8(date_ini,date_end, where_tk,pais, paiscomplete ):

    sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" ALL_COMBINATIONS AS (
        SELECT DISTINCT "ATRIBUIBLE A", SERVICE_NAME AS SERVICIO
        FROM (
            SELECT 'CLARO' AS "ATRIBUIBLE A" FROM DUAL UNION ALL
            SELECT 'CLIENTE' AS "ATRIBUIBLE A" FROM DUAL
        ), (
            SELECT 'INTERNET' AS SERVICE_NAME FROM DUAL UNION ALL
            SELECT 'DATOS' AS SERVICE_NAME FROM DUAL UNION ALL
            SELECT 'AE' AS SERVICE_NAME FROM DUAL
        )
    ),
    TK2 AS (
        SELECT
            "ATRIBUIBLE A",
            SERVICIO,
            CASE
                WHEN SERVICIO = 7 THEN 'INTERNET'
                WHEN SERVICIO = 8 THEN 'DATOS'
                WHEN SERVICIO = 9 THEN 'AE'
                ELSE
                    CASE
                        WHEN "ATRIBUIBLE A" = 'CLARO' THEN 'DATOS_CLARO'
                        WHEN "ATRIBUIBLE A" = 'CLIENTE' THEN 'DATOS_CLIENTE'
                    END
            END A,
            NVL(COUNT(*), 0) CONTAR
        FROM tickets_2
        WHERE
           "FECHA DE CIERRE" >= (SELECT F_INI FROM VARIABLES)
            AND "FECHA DE CIERRE" < (SELECT (F_FIN + 1) FROM VARIABLES)
        GROUP BY "ATRIBUIBLE A", SERVICIO
    ),
    TK_LIST AS (
        SELECT
            "ATRIBUIBLE A",
            CASE
                WHEN BB = 'DATOS_CLIENTE' THEN 'DATOS'
                WHEN BB = 'DATOS_CLARO' THEN 'DATOS'
                ELSE BB
            END SERVICIO,
            CONTAR
        FROM (
            SELECT BB, "ATRIBUIBLE A", SUM(CONTAR) CONTAR
            FROM (
                SELECT A, CONTAR, "ATRIBUIBLE A",
                CASE
                    WHEN A = 'DATOS' AND "ATRIBUIBLE A" = 'CLARO' THEN 'DATOS_CLARO'
                    WHEN A = 'DATOS_CLARO' AND "ATRIBUIBLE A" = 'CLARO' THEN 'DATOS_CLARO'
                    WHEN A = 'DATOS_CLIENTE' AND "ATRIBUIBLE A" = 'CLIENTE' THEN 'DATOS_CLIENTE'
                    WHEN A = 'DATOS' AND "ATRIBUIBLE A" = 'CLIENTE' THEN 'DATOS_CLIENTE'
                    ELSE A
                END BB
                FROM TK2
            ) A
            GROUP BY BB, "ATRIBUIBLE A"
        ) B
    ),
    FINAL_RESULT AS (
        SELECT
            AC."ATRIBUIBLE A", 
            AC.SERVICIO,
            NVL(TL.CONTAR, 0) CONTAR
        FROM
            ALL_COMBINATIONS AC
            LEFT JOIN TK_LIST TL ON AC."ATRIBUIBLE A" = TL."ATRIBUIBLE A" AND AC.SERVICIO = TL.SERVICIO )

    SELECT "ATRIBUIBLE A" as RESPONSABLE, 
        NVL(DATOS, 0) DATOS, 
        NVL(INTERNET, 0) INTERNET, 
        NVL(AE, 0) AE,
         NVL(DATOS, 0) + NVL(INTERNET, 0) + NVL(AE, 0) AS TOTAL
    FROM (
        SELECT * FROM FINAL_RESULT
        PIVOT (
            SUM(CONTAR)
            FOR SERVICIO IN ('DATOS' DATOS, 'INTERNET' INTERNET, 'AE' AE)
        )
    ) A
    ORDER BY
        CASE
            WHEN "ATRIBUIBLE A" = 'CLIENTE' THEN 1
            WHEN "ATRIBUIBLE A" = 'CLARO' THEN 2
        END     
    """
    
    return sql

# ************************************************************
# PAGI 9 Comportamiento Tickets Reactivos y Proactivos
def pag_9(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):

    
    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" TK AS (
        SELECT * FROM TICKETS_2 WHERE  "FECHA DE CIERRE" BETWEEN (SELECT F_INI FROM VARIABLES  ) 
        AND (SELECT TO_DATE(F_FIN)+1 FROM VARIABLES  )
        ), PRO AS(

        SELECT A.*, COUNT(*) CONTAR FROM (
        SELECT "TIPO MONITOREO"  , TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM')) MES,TO_CHAR("FECHA DE CIERRE",'YYYY') ANIO
        FROM TK)A GROUP BY "TIPO MONITOREO"   ,MES,ANIO ORDER BY MES )
        SELECT * FROM (
        SELECT "TIPO MONITOREO" AS MONITOREO, MES,CONTAR FROM PRO)
        PIVOT (
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        )ORDER BY  MONITOREO """

    return sql

# ************************************************************
# Atribución de Tickets Reactivos pag 10
def pag_10(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):

    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" TK AS (
        SELECT * FROM TICKETS_2 WHERE   "FECHA DE CIERRE" BETWEEN (SELECT F_INI FROM VARIABLES  ) 
        AND (SELECT (F_FIN +1) FROM VARIABLES  )
        ), PRO AS(

        SELECT A.*, COUNT(*) CONTAR FROM (
        SELECT "ATRIBUIBLE A", TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM')) MES,TO_CHAR("FECHA DE CIERRE",'YYYY') ANIO
        FROM TK WHERE "TIPO MONITOREO"='MONITOREO REACTIVO')A GROUP BY "ATRIBUIBLE A",MES,ANIO ORDER BY MES )
        SELECT * FROM ( SELECT "ATRIBUIBLE A", MES,CONTAR FROM PRO)
        PIVOT (  AVG(CONTAR)   FOR MES IN ({cadena_mes})  )ORDER BY  "ATRIBUIBLE A" 
    """

    return sql 

# ==============================
# Causas Monitoreo Reactivo Atribuibles al Cliente PAG 11
def pag_11(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):
    
    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" TK AS (
        SELECT * FROM TICKETS_2 
        WHERE "TIPO MONITOREO"='MONITOREO REACTIVO' and "ATRIBUIBLE A"='CLIENTE'  
          AND "FECHA DE CIERRE" BETWEEN (SELECT F_INI FROM VARIABLES  ) 
        AND (SELECT (F_FIN +1) FROM VARIABLES  )
        ), AGRUPACION AS(
        select FALLA,SUBFALLA,"CODIGO DE CIERRE",TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM')) MES,COUNT(*) CONTAR from tk
        GROUP BY FALLA,SUBFALLA,"CODIGO DE CIERRE",TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM'))
        )
        SELECT * FROM(
        SELECT FALLA,SUBFALLA,"CODIGO DE CIERRE", MES,CONTAR FROM AGRUPACION
        )
        PIVOT(
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        )
    """

    return sql 

# ==============================
# Principales Causas Tickets Reactivos Atribuibles a Claro || PAG 12 
def pag_12(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):

    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" TK AS (
        SELECT * FROM TICKETS_2 
        WHERE "TIPO MONITOREO"='MONITOREO REACTIVO' and "ATRIBUIBLE A"='CLARO' 
        AND "FECHA DE CIERRE" BETWEEN (SELECT F_INI FROM VARIABLES  ) 
        AND (SELECT  (F_FIN +1) FROM VARIABLES  )
        ), AGRUPACION AS(
        select FALLA,SUBFALLA,"CODIGO DE CIERRE",TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM')) MES,COUNT(*) CONTAR from tk
        GROUP BY FALLA,SUBFALLA,"CODIGO DE CIERRE",TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM'))
        )
        SELECT * FROM(
        SELECT FALLA,SUBFALLA,"CODIGO DE CIERRE", MES,CONTAR FROM AGRUPACION
        )
        PIVOT(
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        )
    """

    return sql 

# ==============================
# Tiempos de solución Tickets Reactivos atribuibles a Claro PAG 13
def pag_13(date_ini,date_end, where_tk,pais, paiscomplete ):

    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" tk AS (
            SELECT *
            FROM tickets_2
            WHERE
                "TIPO MONITOREO" = 'MONITOREO REACTIVO'
                AND "ATRIBUIBLE A" = 'CLARO'
                AND "FECHA DE CIERRE" BETWEEN (
                    SELECT F_INI
                    FROM   variables
                ) AND (
                    SELECT  TO_DATE(f_fin + 1)
                    FROM    variables
                )
        ), agrupacion AS (
            SELECT
               "ATRIBUIBLE A",
                "RANGO SOLUCION",
                TO_NUMBER(to_char("FECHA DE CIERRE", 'MM')) mes,
                COUNT(*) contar
            FROM
                tickets_2
            GROUP BY
                "ATRIBUIBLE A",
                "RANGO SOLUCION",
                TO_NUMBER(to_char("FECHA DE CIERRE", 'MM'))
        )
        SELECT A.*,
        CASE 
            WHEN "RANGO SOLUCION"='RANGO DE 0 A 0.5 HORAS' THEN 1
            WHEN "RANGO SOLUCION"='RANGO DE 0.5 A 1 HORAS' THEN 2
            WHEN "RANGO SOLUCION"='RANGO DE 1 A 2 HORAS' THEN 3
            WHEN "RANGO SOLUCION"='RANGO DE 2 A 4 HORAS' THEN 4
            WHEN "RANGO SOLUCION"='RANGO DE 4 A 8 HORAS' THEN 5
            WHEN "RANGO SOLUCION"='RANGO DE 8 A 12 HORAS' THEN 6
            WHEN "RANGO SOLUCION"='RANGO MAS DE 12 HORAS' THEN 7
            END ORDEN
            FROM (
        SELECT * FROM(
        SELECT "ATRIBUIBLE A", "RANGO SOLUCION", MES,CONTAR FROM AGRUPACION
        )
        PIVOT(
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        ))A ORDER BY ORDEN ASC
    """

    return sql

# ==============================
# Top 10 enlaces – Tickets atribuibles a Claro  Monitoreo Reactivo y Proactivo || PAG 14
def pag_14(date_ini,date_end, where_tk,pais, paiscomplete ):
    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" PROCESO AS(
        select * from(
        select ENLACE,UBICACION,"TIPO MONITOREO" from tickets_2 where "ATRIBUIBLE A" = 'CLARO' 
        )
        pivot (
            COUNT("TIPO MONITOREO")
          FOR "TIPO MONITOREO" IN ('MONITOREO PROACTIVO', 'MONITOREO REACTIVO')
        ))
        SELECT * FROM (
        SELECT ENLACE, UBICACION,"'MONITOREO PROACTIVO'" PROACTIVO,"'MONITOREO REACTIVO'" REACTIVO,"'MONITOREO PROACTIVO'"+"'MONITOREO REACTIVO'" TT FROM PROCESO
        )A WHERE ROWNUM <= 10 ORDER BY TT DESC
    """
    return sql
# ==============================
# Atribución de Tickets Proactivos || PAG 15 
def pag_15(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):
    sql =  sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" PRO AS(
        SELECT A.*, COUNT(*) CONTAR FROM (
        SELECT "ATRIBUIBLE A", TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM')) MES,TO_CHAR("FECHA DE CIERRE",'YYYY') ANIO
        FROM TK WHERE "TIPO MONITOREO"='MONITOREO PROACTIVO')A GROUP BY "ATRIBUIBLE A",MES,ANIO ORDER BY MES )
        SELECT * FROM (
        SELECT "ATRIBUIBLE A", MES,CONTAR FROM PRO)
        PIVOT (
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        )ORDER BY  "ATRIBUIBLE A"
    """
    return sql

# ==============================
# Causas Monitoreo Proactivo Atribuibles al Cliente
def pag_16(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):

    sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" AGRUPACION AS(
        select FALLA,SUBFALLA,"CODIGO DE CIERRE",TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM')) MES,COUNT(*) CONTAR from tickets_2
        GROUP BY FALLA,SUBFALLA,"CODIGO DE CIERRE",TO_NUMBER(TO_CHAR("FECHA DE CIERRE",'MM'))
        )
        SELECT * FROM(
        SELECT FALLA,SUBFALLA,"CODIGO DE CIERRE", MES,CONTAR FROM AGRUPACION
        )
        PIVOT(
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        )
    """

    return sql

# ==============================
# Tiempos de Restauración Fallas de Energía en Sitios del Cliente || PAG 17
def pag_17(date_ini,date_end, where_tk,pais, paiscomplete ):

    sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" PROCESO AS(
        select * from(
        select  "RANGO SOLUCION" from TICKETS_2 where "CODIGO DE CIERRE" = 'SERVICIO_ENERGIA COMERCIAL' 
        and "ATRIBUIBLE A"='CLIENTE'
        ))

        select "RANGO SOLUCION","Total",ROUND("% del Total",2),ROUND("% del Rango",2),
        CASE 
            WHEN "RANGO SOLUCION"='RANGO DE 0 A 0.5 HORAS' THEN 1
            WHEN "RANGO SOLUCION"='RANGO DE 0.5 A 1 HORAS' THEN 2
            WHEN "RANGO SOLUCION"='RANGO DE 1 A 2 HORAS' THEN 3
            WHEN "RANGO SOLUCION"='RANGO DE 2 A 4 HORAS' THEN 4
            WHEN "RANGO SOLUCION"='RANGO DE 4 A 8 HORAS' THEN 5
            WHEN "RANGO SOLUCION"='RANGO DE 8 A 12 HORAS' THEN 6
            WHEN "RANGO SOLUCION"='RANGO MAS DE 12 HORAS' THEN 7
            END ORDEN
        from (
        SELECT 
          "RANGO SOLUCION",
          COUNT(*) AS "Total",
          COUNT(*) * 100 / SUM(COUNT(*)) OVER() AS "% del Total",
          COUNT(*) * 100 / SUM(COUNT(*)) OVER(PARTITION BY "RANGO SOLUCION") AS "% del Rango"
        FROM PROCESO
        GROUP BY "RANGO SOLUCION")A ORDER BY ORDEN ASC
    """
    
    return sql

# ==============================
#  Top 20 de Sitios Reincidentes por Energía || PAG 18
def pag_18(date_ini,date_end, where_tk,pais, paiscomplete ):

    sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" PROCESO AS(
        select * from(
        select  ENLACE,UBICACION,"DURACION TICKET (horas)" 
            from TICKETS_2 where "CODIGO DE CIERRE" = 'SERVICIO_ENERGIA COMERCIAL'  ))
        SELECT * FROM (
        SELECT ENLACE,UBICACION,COUNT(ENLACE) TT , ROUND(AVG("DURACION TICKET (horas)"),2) TT_T 
            FROM PROCESO  GROUP BY ENLACE,UBICACION)A WHERE ROWNUM <=20 ORDER BY TT DESC
    """

    return sql

# ==============================
# Tiempos de diagnóstico, escalación y solución de Tickets Proactivos atribuibles a Claro || pag 20
def pag_19(date_ini,date_end, where_tk,pais, paiscomplete, cadena_mes):

    sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f""" 
        agrupacion AS (
            SELECT "ATRIBUIBLE A", "RANGO SOLUCION",
                TO_NUMBER(to_char("FECHA DE CIERRE", 'MM')) mes,
                COUNT(*) contar
            FROM
                TICKETS_2
            WHERE
                "TIPO MONITOREO" = 'MONITOREO PROACTIVO'
                AND "ATRIBUIBLE A" = 'CLARO'   
            GROUP BY
                "ATRIBUIBLE A", "RANGO SOLUCION",
                TO_NUMBER(to_char("FECHA DE CIERRE", 'MM'))
        )
        SELECT A.*,
        CASE 
            WHEN "RANGO SOLUCION"='RANGO DE 0 A 0.5 HORAS' THEN 1
            WHEN "RANGO SOLUCION"='RANGO DE 0.5 A 1 HORAS' THEN 2
            WHEN "RANGO SOLUCION"='RANGO DE 1 A 2 HORAS' THEN 3
            WHEN "RANGO SOLUCION"='RANGO DE 2 A 4 HORAS' THEN 4
            WHEN "RANGO SOLUCION"='RANGO DE 4 A 8 HORAS' THEN 5
            WHEN "RANGO SOLUCION"='RANGO DE 8 A 12 HORAS' THEN 6
            WHEN "RANGO SOLUCION"='RANGO MAS DE 12 HORAS' THEN 7
            END ORDEN
            FROM (
        SELECT * FROM(
        SELECT "ATRIBUIBLE A", "RANGO SOLUCION", MES,CONTAR FROM AGRUPACION
        )
        PIVOT(
          AVG(CONTAR) 
          FOR MES IN ({cadena_mes})
        ))A ORDER BY ORDEN ASC 
    """ 

    return sql

# ==============================
# CONSULTA GENERAL 
def pag_20(date_ini,date_end, where_tk,pais, paiscomplete  ):

    sql = sql_base(date_ini,date_end, where_tk,pais, paiscomplete) + f"""  PROCESO AS(
        select * from(
        select  ENLACE,UBICACION,PAIS,"T TICKET ACTIVO (horas)","FECHA DE CIERRE" from tk where "ATRIBUIBLE A" = 'CLARO' AND problem_type = 'CAIDA TOTAL'
            ))
        SELECT * FROM (
        SELECT ENLACE,UBICACION,TT_T, ROUND(( 1 - ( TT_T / TT_H ) )*100,3) "DISPONIBILIDAD MENSUAL", PAIS FROM (
        SELECT ENLACE,UBICACION,PAIS,MAX("FECHA DE CIERRE"), sum("T TICKET ACTIVO (horas)") TT_T, 
        ( 1 + trunc(last_day(MAX("FECHA DE CIERRE"))) - trunc(MAX("FECHA DE CIERRE"), 'MM') ) * 24 TT_H
        FROM PROCESO  GROUP BY ENLACE,UBICACION, PAIS)A  ORDER BY TT_T DESC)C WHERE "DISPONIBILIDAD MENSUAL" >= 95 

    """

    return sql 

# ==============================


# ==============================


# ==============================

