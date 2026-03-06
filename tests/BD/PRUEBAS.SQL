---
-- COLOCAR 
-- consulta que estba MODIFICANDO EL MARLON 
---

with
VARIABLES AS (
SELECT 1 COD ,'01012026' F_INI,'31012026' F_FIN, 'GUATEMALA' PAIS FROM DUAL
),tickets_enlaces as (
   select probsummarym1."NUMBER",
          tg_enlace,
          (
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
          ) enlace,
          tg_enlace_destino,
          tg_company_cnoc,
          company,
          (
             case
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
                and name like '%Monitoreo%'
              group by key_char
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
  probsummarym1.company LIKE '%BANCO DE DESARROLLO RURAL%'
  OR probsummarym2.TG_COMPANY_CNOC LIKE '%BANCO DE DESARROLLO RURAL%'
  OR probsummarym1.brief_description LIKE '%BANCO DE DESARROLLO RURAL%'
  OR probsummarym1.action LIKE '%BANCO DE DESARROLLO RURAL%'
  --OR tk.tg_enlace_destino LIKE '%BANCO DE DESARROLLO RURAL%'
  OR tg_enlace LIKE '%CC\_BANRURAL\_GT%' ESCAPE '\'
  )
      and probsummarym1.assignment in ( 'CNOC',
                                        'CNOC_CBO_PROACTIVO',
                                        'CNOC_CBO_REACTIVO',
                                        'CNOC_MASIVO',
                                        'GESTION DE DATOS N1',
                                        'GESTION N1_CBO',
                                        'GT - ACC. EMPRESARIAL - NOC',
                                        'SOPORTE_N1_XT',
                                        'SOPORTE_N2_XT' )
      and ( probsummarym1.resolved_group in ( 'CNOC',
                                              'CNOC_CBO_PROACTIVO',
                                              'CNOC_CBO_REACTIVO',
                                              'CNOC_MASIVO',
                                              'GESTION DE DATOS N1',
                                              'GESTION N1_CBO',
                                              'GT - ACC. EMPRESARIAL - NOC',
                                              'SOPORTE_N1_XT',
                                              'SOPORTE_N2_XT' )
       or probsummarym1.resolved_group is null )
      and ( probsummarym1.close_time between (
      select F_INI
        from variables
   ) and (
      select F_FIN
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
      select tk."NUMBER" ticket,
             tk.enlace,
             tk.tg_enlace_destino ubicacion,
             case
                when regexp_substr(
                   tk.enlace,
                   '_GT_',
                   1,
                   1,
                   'i'
                ) = '_GT_'
                    or enlace like '%T'
                    or enlace like '%GUATEMALA%' then
                   'GUATEMALA'
                when regexp_substr(
                   tk.enlace,
                   '_SV_',
                   1,
                   1,
                   'i'
                ) = '_SV_'
                    or enlace like '%SV'
                    or enlace like '%SALVADOR%' then
                   'EL SALVADOR'
                when regexp_substr(
                   tk.enlace,
                   '_CR_',
                   1,
                   1,
                   'i'
                ) = '_CR_'
                    or enlace like '%OC'
                    or enlace like '%COSTA RICA%' then
                   'COSTA RICA'
                when regexp_substr(
                   tk.enlace,
                   '_NI_',
                   1,
                   1,
                   'i'
                ) = '_NI_'
                    or enlace like '%ON'
                    or enlace like '%NICARAGUA%' then
                   'NICARAGUA'
                when regexp_substr(
                   tk.enlace,
                   '_HN_',
                   1,
                   1,
                   'i'
                ) = '_HN_'
                    or enlace like '%OH'
                    or enlace like '%HONDURAS%' then
                   'HONDURAS'
                when ( tk.enlace like 'FG%'
                    or tk.enlace like '%FEMTO_GT%' ) then
                   'FEMTOCELDA GUATEMALA'
                when ( tk.enlace like 'FS%'
                    or tk.enlace like '%FEMTO_SV%' ) then
                   'FEMTOCELDA EL SALVADOR'
                when ( tk.enlace like 'FH%'
                    or tk.enlace like '%FEMTO_HN%' ) then
                   'FEMTOCELDA HONDURAS'
                when ( tk.enlace like '%FEMTO_NI%' ) then
                   'FEMTOCELDA NICARAGUA'
                when ( tk.enlace like 'F%' ) then
                   'FEMTOCELDA'
                else
                   (
                      case
                         when device2m1.tg_country_code = 'GT' then
                            'GUATEMALA'
                         when device2m1.tg_country_code = 'SV' then
                            'EL SALVADOR'
                         when device2m1.tg_country_code = 'CR' then
                            'COSTA RICA'
                         when device2m1.tg_country_code = 'NI' then
                            'NICARAGUA'
                         when device2m1.tg_country_code = 'HN' then
                            'HONDURAS'
                         when device2m1.tg_country_code = 'PA' then
                            'PANAMA'
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
                   when tk.category = 'DX - BOLETA MAL ABIERTA'
                      and tk.opened_by = 'tmipuser' then
                      'CLARO'
                   when tk.res_anal_code = 'CALL CENTER'
                       or tk.res_anal_code = 'TEMIP' then
                      'CLARO'
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
             ( coalesce(
                "Pending Customer (horas)",
                0
             ) + coalesce(
                "WO Pending Customer (horas)",
                0
             ) + coalesce(
                "Resolved (horas)",
                0
             ) + coalesce(
                "Monitoreo (horas)",
                0
             ) + coalesce(
                "Dictamen (horas)",
                0
             ) ) tt_resta,
             tk.close_time "FECHA DE CIERRE",
             tk.open_time "FECHA DE APERTURA",
             tk.res_anal_code "CODIGO DE CIERRE",
             tk.problem_type,
             tg_id_clase_servicio servicio,
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
),t_tickets_cerrados_cnoc_lite as (
   select tk.*,
          case
             when ( "T TICKET ACTIVO (horas)" >= 0 )
                and ( "T TICKET ACTIVO (horas)" <= 0.5 ) then
                'RANGO DE 0 A 0.5 HORAS'
             when ( "T TICKET ACTIVO (horas)" > 0.5 )
                and ( "T TICKET ACTIVO (horas)" <= 1 ) then
                'RANGO DE 0.5 A 1 HORAS'
             when ( "T TICKET ACTIVO (horas)" > 1 )
                and ( "T TICKET ACTIVO (horas)" <= 2 ) then
                'RANGO DE 1 A 2 HORAS'
             when ( "T TICKET ACTIVO (horas)" > 2 )
                and ( "T TICKET ACTIVO (horas)" <= 4 ) then
                'RANGO DE 2 A 4 HORAS'
             when ( "T TICKET ACTIVO (horas)" > 4 )
                and ( "T TICKET ACTIVO (horas)" <= 8 ) then
                'RANGO DE 4 A 8 HORAS'
             when ( "T TICKET ACTIVO (horas)" > 8 )
                and ( "T TICKET ACTIVO (horas)" <= 12 ) then
                'RANGO DE 8 A 12 HORAS'
             when ( "T TICKET ACTIVO (horas)" > 12 ) then
                'RANGO MAS DE 12 HORAS'
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
),
TICKETS_2 AS (
select ticket,
       enlace,
       ubicacion,
       pais,
       "MES CIERRE",
       tg_company_cnoc,
       cliente,
       "PROBLEMA REPORTADO",
       "DETALLE PROBLEMA REPORTADO",
       falla,
       subfalla,
       "SUB SUBFALLA",
       "ATRIBUIBLE A",
       "DURACION TICKET (horas)" as "T VIDA TICKET (horas)",
       "T TICKET ACTIVO (horas)",
       "FECHA DE CIERRE",
       "FECHA DE APERTURA",
       "CODIGO DE CIERRE",
       problem_type,
       servicio,
       "GRUPO QUE RESOLVIO",
       "TIPO MONITOREO",
       "RANGO SOLUCION",
       "RANGO SOLUCION 2",
       "DURACION TICKET (horas)",
       opened_by,
       "DURACION TICKET (horas)" as "T TICKET ACTIVO"
  from t_tickets_cerrados_cnoc_lite
  WHERE PAIS ='GUATEMALA')
, TK AS ( SELECT * FROM TICKETS_2)
--WHERE 
--ID_INTERNO=(SELECT COD FROM VARIABLES) AND 
--"FECHA DE CIERRE" BETWEEN (SELECT F_INI FROM VARIABLES) AND (SELECT  to_date(F_FIN) +1 FROM VARIABLES) )
, TK_ATRIBUCION_CLIENTE AS ( SELECT * FROM TICKETS_2 WHERE  "ATRIBUIBLE A"='CLIENTE' )
, TK_PROACTIVOS         AS ( SELECT "TIPO MONITOREO" FROM TK  )
, RANGO_SOLUCION        AS ( SELECT "RANGO SOLUCION 2" R, COUNT("RANGO SOLUCION 2") CONTAR FROM TICKETS_2 GROUP BY "RANGO SOLUCION 2" )

select * from RANGO_SOLUCION;

-----
SELECT * FROM RANGO_SOLUCION;
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
    NULLIF((SELECT COUNT(*) FROM ENLACES),0) TT_ENLACES ,
    NULLIF((SELECT COUNT(*) FROM TK_PROACTIVOS WHERE "TIPO MONITOREO"='MONITOREO PROACTIVO'),0) PRO,
    NULLIF((SELECT avg("T TICKET ACTIVO (horas)") FROM TK),0) PROMEDIO,
    NULLIF((SELECT COUNT(ENLACE) ENLACE FROM (SELECT COUNT(ENLACE) ENLACE FROM TK  GROUP BY ENLACE HAVING COUNT(ENLACE)>=2)),0) INDI
    FROM DUAL) A 
    ;
  
  