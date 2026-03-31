-- COD 1
{{* ********************************************************************* *}}

update p_service_m
   set
   id_interno = '1'
 where probsummarym1.company like '%BANCO DE LOS TRABAJADORES%'
   and ID_SM not like '%XT'
   and pais = 'GT';

  
        from t_tickets_cerrados_cnoc_lite
       where ( (  probsummarym1.company like '%BANCO DE LOS TRABAJADORES%' )
          or (  probsummarym1.company like '%BANCO DE LOS TRABAJADORES%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO DE LOS TRABAJADORES%'
          or probsummarym1.brief_description like 'BANCO DE LOS TRABAJADORES%'
          or probsummarym1.action like '%BANCO DE LOS TRABAJADORES%'
          -- tg_enlace_destino like '%BANCO DE LOS TRABAJADORES%'
          or tg_enlace like '%CC\_BANTRAB\_GT%' escape '\'
          
           ) )
-- FIN 1
{{* ********************************************************************* *}}

-- COD 2
update p_service_m
   set
   id_interno = '2'
 where probsummarym1.company like '%FICOHSA%'
   and ID_SM not like '%XT'
   and pais = 'GT'


        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FICOHSA%'
          or probsummarym2.TG_COMPANY_CNOC like '%FICOHSA%'
          or probsummarym1.brief_description like '%FICOHSA%'
          or probsummarym1.action like '%FICOHSA%'
          -- tg_enlace_destino like '%FICOHSA%' 
          )
         and pais = 'GUATEMALA'
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
    -- FIN 2
{{* ********************************************************************* *}}

-- COD 3
update p_service_m
   set
   id_interno = '3'
 where probsummarym1.company like '%BANCO AGROMERCANTIL DE GUATEMALA%'
   and ID_SM not like 'XT %'
   
   ;
 

        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BANCO AGROMERCANTIL DE GUATEMALA%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO AGROMERCANTIL DE GUATEMALA%'
          or probsummarym1.brief_description like '%BANCO AGROMERCANTIL DE GUATEMALA%'
          or probsummarym1.action like '%BANCO AGROMERCANTIL DE GUATEMALA%'
          -- tg_enlace_destino like '%BANCO AGROMERCANTIL DE GUATEMALA%'
          or tg_enlace like '%CC\_BAM\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );

-- FIN 3
{{* ********************************************************************* *}}

    -- COD 4
update p_service_m
   set
   id_interno = '4'
 where probsummarym1.company like '%BANCO AZTECA DE GUATEMALA%'
   and ID_SM not like '%XT'
   ;
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BANCO AZTECA DE GUATEMALA S.A.%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO AZTECA DE GUATEMALA S.A.%'
          or probsummarym1.brief_description like '%BANCO AZTECA DE GUATEMALA S.A.%'
          or probsummarym1.action like 'BANCO AZTECA DE GUATEMALA S.A.%'
          -- tg_enlace_destino like '%BANCO AZTECA DE GUATEMALA S.A.%'
          or tg_enlace like '%CC\_AZTECA\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA' 
	--and ID_SM not like '%XT' 
   );
-- FIN 4
{{* ********************************************************************* *}}

    -- COD 5
update p_service_m
   set
   id_interno = '5'
 where probsummarym1.company like '%BANCO DE DESARROLLO RURAL%'
   and ID_SM not like '%XT'
   and pais = 'GT'
   
   ;
 
        from t_tickets_cerrados_cnoc_lite
       where (  
         probsummarym1.company like '%BANCO DE DESARROLLO RURAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO DE DESARROLLO RURAL%'
          or probsummarym1.brief_description like '%BANCO DE DESARROLLO RURAL%'
          or probsummarym1.action like '%BANCO DE DESARROLLO RURAL%'
          -- tg_enlace_destino like '%BANCO DE DESARROLLO RURAL%'
          or tg_enlace like '%CC\_BANRURAL\_GT%' escape '\'
          
           )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA' 
	-- and ID_SM not like '%XT' 
   );
   

    -- FIN 5
 {{* ********************************************************************* *}}
   
{{* ********************************************************************* *}}

-- COD 6
update p_service_m
   set
   id_interno = '6'
 where probsummarym1.company like '%BANCO G'
                    || '&'
                    || 'T CONTINENTAL%'
   and ID_SM not like '%XT';
 

        from t_tickets_cerrados_cnoc_lite
       where ( (  probsummarym1.company like '%BANCO G' || '&' || 'T CONTINENTAL%' )
          or (
			--probsummarym2.TG_COMPANY_CNOC LIKE '%BANCO G' || '&' || 'T CONTINENTAL%' 
			--OR t_tickets_cerrados_cnoc_lite.COMPANY LIKE '%BANCO G' || '&' || 'T CONTINENTAL%' 
			--OR 
   or probsummarym1.brief_description like '%BANCO G' || '&' || 'T CONTINENTAL%'
   or probsummarym1.action like '%BANCO G' || '&' || 'T CONTINENTAL%'
   or tg_enlace like '%CC\_GYT\_INTERNET%' escape '\'
   or tg_enlace like '%CC\_GYT\_GT%' escape '\'
   or probsummarym1.action like '%CC\_GYT\_AGENCIA_%' escape '\'
   or probsummarym1.action like '%AG.%'
         -- tg_enlace_destino like '%BANCO G'|| '&'|| 'T CONTINENTAL%'
   or tg_enlace like '%CC\_GYT\_INTERNET%' escape '\'
   or tg_enlace like '%CC\_GYT\_GT%' escape '\'
   or probsummarym1.action like '%CC\_GYT\_AGENCIA_%' escape '\'
   or probsummarym1.action like '%AG.%' 
   ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA' 
	--and ID_SM not like '%XT' 
   );
{{* ********************************************************************* *}}
-- FIN 6

    -- COD 7
update p_service_m
   set
   id_interno = '7'
 where ( enlace = '19600012T'
    or enlace = '19600013T'
    or enlace = '19600016T'
    or enlace = '212800007T'
    or enlace = '212900002T'
    or enlace = '212900007T'
    or enlace = '212900009T'
    or enlace = '213000006T'
    or enlace = '213000007T'
    or enlace = '213200002T'
    or enlace = '213300003T'
    or enlace = '213400009T'
    or enlace = '213600002T'
    or enlace = '213700002T'
    or enlace = '213900003T'
    or enlace = '214000004T'
    or enlace = '214100001T'
    or enlace = '214200005T'
    or enlace = '214300001T'
    or enlace = '214400004T'
    or enlace = '214500002T'
    or enlace = '234600002T'
    or enlace = '236100007T'
    or enlace = '2800008T'
    or enlace = '312600001T'
    or enlace = '312600003T'
    or enlace = '366300002T'
    or enlace = '371200002T'
    or enlace = '402000003T'
    or enlace = '404500002T'
    or enlace = '405900002T'
    or enlace = '405900004T'
    or enlace = '432800008T'
    or enlace = '58700010T'
    or enlace = '58800008T'
    or enlace = '58900007T'
    or enlace = '59600007T'
    or enlace = '59900010T'
    or enlace = '62400008T'
    or enlace = '86100014T'
    or enlace = '86100018T'
    or enlace = '86100023T'
    or enlace = '97100043T'
    or enlace = '97100068T'
    or enlace = '97100070T'
    or enlace = '97100071T'
    or enlace = '97100072T'
    or enlace = '97100073T'
    or enlace = '97100080T'
    or enlace = '97100081T'
    or enlace = '97100082T'
    or enlace = '97100083T'
    or enlace = '97100085T'
    or enlace = '97100089T'
    or enlace = '97100091T'
    or enlace = '97100092T'
    or enlace = '97100093T'
    or enlace = '97100094T'
    or enlace = '97100095T'
    or enlace = '97100096T'
    or enlace = '97100098T'
    or enlace = '97100099T'
    or enlace = '97100100T'
    or enlace = '97100101T'
    or enlace = '97100102T'
    or enlace = '97100103T'
    or enlace = '97100104T'
    or enlace = '97100105T'
    or enlace = '97100106T'
    or enlace = '97100110T'
    or enlace = '97100111T'
    or enlace = '97100112T'
    or enlace = '97100113T'
    or enlace = '97100114T'
    or enlace = '97100116T'
    or enlace = '97100118T'
    or enlace = '97100119T'
    or enlace = '97100120T'
    or enlace = '97100121T'
    or enlace = '97100122T'
    or enlace = '97100124T'
    or enlace = '97100125T'
    or enlace = '97100126T'
    or enlace = '97100127T'
    or enlace = '97100128T'
    or enlace = '97100129T'
    or enlace = '97100130T'
    or enlace = '97100131T'
    or enlace = '97100132T'
    or enlace = '97100133T'
    or enlace = '97100134T'
    or enlace = '97100135T'
    or enlace = '97100136T'
    or enlace = '97100137T'
    or enlace = '97100138T'
    or enlace = '97100139T'
    or enlace = '97100140T'
    or enlace = '97100141T'
    or enlace = '97100142T'
    or enlace = '97100144T'
    or enlace = '97100145T'
    or enlace = '97100146T'
    or enlace = '97100147T'
    or enlace = '97100148T'
    or enlace = '97100149T'
    or enlace = '97100153T'
    or enlace = '97100154T'
    or probsummarym1.company like '%ALIMENTOS, S.A.%'
    or probsummarym1.company like '%CENTRAL DE ALIMENTOS, S.A.%'
    or probsummarym1.company like '%CERVECERIA CENTROAMERICANA,  S.A.%'
    or probsummarym1.company like '%CERVECERIA CENTROAMERICANA, S.A.%'
    or probsummarym1.company like '%CERVECERIA DEL SUR, S.A.%'
    or probsummarym1.company like '%COMERCIAL LOS HERMANOS S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA ALINOR S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA COBANERA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA HUEHUETECA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA IZABAL,S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA JUTIAPANECA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA LA CEIBA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA LA NUEVA S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA LOS ALTOS, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA LOS CIPRESES, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA MALACATAN, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA MARAVILLA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA MARQUENSE, S.,A.%'
    or probsummarym1.company like '%DISTRIBUIDORA MAZATECA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA PANAMERICANA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA QUICHE, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA SAGITARIO, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA SANTA LUCIA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA SANTA ROSA, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA SATURNO, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA SAUZALITO, S.A.%'
    or probsummarym1.company like '%DISTRIBUIDORA ULTRARAPIDA%'
    or probsummarym1.company like '%EMBOTELLADORES UNIDOS, S.A.%'
    or probsummarym1.company like '%FUNDACION CASTILLO CORDOVA%'
    or probsummarym1.company like '%INDUSTRIAS AGRICOLAS CENTRO AMERICANAS S.A.%'
    or probsummarym1.company like '%INVERSIONES CENTROAMERICANAS S.A.%'
    or probsummarym1.company like '%INVERSIONES CENTROAMERICANAS, S.A.%'
    or probsummarym1.company like '%INYECTORES DE PLASTICO, S.A.%'
    or probsummarym1.company like '%MADERAS DE CENTRO AMERICA S.A.%'
    or probsummarym1.company like '%PRONE, PROMOCIONES Y NEGOCIOS, S.A.%' )
   and ID_SM not like '%XT';

insert into tickets_2 (
   "TICKET",
   "ENLACE",
   "UBICACION",
   "PAIS",
   "MES CIERRE",
   "TG_COMPANY_CNOC",
   "CLIENTE",
   "PROBLEMA REPORTADO",
   "DETALLE PROBLEMA REPORTADO",
   "FALLA",
   "SUBFALLA",
   "SUB SUBFALLA",
   "ATRIBUIBLE A",
   "T TICKET ACTIVO (horas)",
   "FECHA DE CIERRE",
   "CODIGO DE CIERRE",
   "PROBLEM_TYPE",
   "RANGO SOLUCION",
   "RANGO SOLUCION 2",
   "DURACION TICKET (horas)",
   "TIPO MONITOREO",
   "SERVICIO",
   id_interno
)
   select "TICKET",
          "ENLACE",
          "UBICACION",
          "PAIS",
          "MES CIERRE",
          "TG_COMPANY_CNOC",
          "CLIENTE",
          substr(
             "PROBLEMA REPORTADO",
             1,
             3990
          ) as "PROBLEMA REPORTADO",
          substr(
             "DETALLE PROBLEMA REPORTADO",
             1,
             3990
          ) as "DETALLE PROBLEMA REPORTADO",
          "FALLA",
          "SUBFALLA",
          "SUB SUBFALLA",
          "ATRIBUIBLE A",
          "T TICKET ACTIVO (horas)",
          "FECHA DE CIERRE",
          "CODIGO DE CIERRE",
          "PROBLEM_TYPE",
          "RANGO SOLUCION",
          "RANGO SOLUCION 2",
          "DURACION TICKET (horas)",
          "TIPO MONITOREO",
          "SERVICIO",
          '7' as id_interno
     from (
      select "TICKET",
             "ENLACE",
             "UBICACION",
             "PAIS",
             "MES CIERRE",
             "TG_COMPANY_CNOC",
             "CLIENTE",
             substr(
                "PROBLEMA REPORTADO",
                3980,
                1
             ) "PROBLEMA REPORTADO",
             substr(
                "DETALLE PROBLEMA REPORTADO",
                3980,
                1
             ) "DETALLE PROBLEMA REPORTADO",
             "FALLA",
             "SUBFALLA",
             "SUB SUBFALLA",
             "ATRIBUIBLE A",
             "T TICKET ACTIVO (horas)",
             "FECHA DE CIERRE",
             "CODIGO DE CIERRE",
             "PROBLEM_TYPE",
             "SERVICIO",
             "RANGO SOLUCION",
             "DURACION TICKET (horas)",
             "TIPO MONITOREO",
             "RANGO SOLUCION 2"
        from t_tickets_cerrados_cnoc_lite
       where ( ( enlace = '19600012T'
          or enlace = '19600013T'
          or enlace = '19600016T'
          or enlace = '212800007T'
          or enlace = '212900002T'
          or enlace = '212900007T'
          or enlace = '212900009T'
          or enlace = '213000006T'
          or enlace = '213000007T'
          or enlace = '213200002T'
          or enlace = '213300003T'
          or enlace = '213400009T'
          or enlace = '213600002T'
          or enlace = '213700002T'
          or enlace = '213900003T'
          or enlace = '214000004T'
          or enlace = '214100001T'
          or enlace = '214200005T'
          or enlace = '214300001T'
          or enlace = '214400004T'
          or enlace = '214500002T'
          or enlace = '234600002T'
          or enlace = '236100007T'
          or enlace = '2800008T'
          or enlace = '312600001T'
          or enlace = '312600003T'
          or enlace = '366300002T'
          or enlace = '371200002T'
          or enlace = '402000003T'
          or enlace = '404500002T'
          or enlace = '405900002T'
          or enlace = '405900004T'
          or enlace = '432800008T'
          or enlace = '58700010T'
          or enlace = '58800008T'
          or enlace = '58900007T'
          or enlace = '59600007T'
          or enlace = '59900010T'
          or enlace = '62400008T'
          or enlace = '86100014T'
          or enlace = '86100018T'
          or enlace = '86100023T'
          or enlace = '97100043T'
          or enlace = '97100068T'
          or enlace = '97100070T'
          or enlace = '97100071T'
          or enlace = '97100072T'
          or enlace = '97100073T'
          or enlace = '97100080T'
          or enlace = '97100081T'
          or enlace = '97100082T'
          or enlace = '97100083T'
          or enlace = '97100085T'
          or enlace = '97100089T'
          or enlace = '97100091T'
          or enlace = '97100092T'
          or enlace = '97100093T'
          or enlace = '97100094T'
          or enlace = '97100095T'
          or enlace = '97100096T'
          or enlace = '97100098T'
          or enlace = '97100099T'
          or enlace = '97100100T'
          or enlace = '97100101T'
          or enlace = '97100102T'
          or enlace = '97100103T'
          or enlace = '97100104T'
          or enlace = '97100105T'
          or enlace = '97100106T'
          or enlace = '97100110T'
          or enlace = '97100111T'
          or enlace = '97100112T'
          or enlace = '97100113T'
          or enlace = '97100114T'
          or enlace = '97100116T'
          or enlace = '97100118T'
          or enlace = '97100119T'
          or enlace = '97100120T'
          or enlace = '97100121T'
          or enlace = '97100122T'
          or enlace = '97100124T'
          or enlace = '97100125T'
          or enlace = '97100126T'
          or enlace = '97100127T'
          or enlace = '97100128T'
          or enlace = '97100129T'
          or enlace = '97100130T'
          or enlace = '97100131T'
          or enlace = '97100132T'
          or enlace = '97100133T'
          or enlace = '97100134T'
          or enlace = '97100135T'
          or enlace = '97100136T'
          or enlace = '97100137T'
          or enlace = '97100138T'
          or enlace = '97100139T'
          or enlace = '97100140T'
          or enlace = '97100141T'
          or enlace = '97100142T'
          or enlace = '97100144T'
          or enlace = '97100145T'
          or enlace = '97100146T'
          or enlace = '97100147T'
          or enlace = '97100148T'
          or enlace = '97100149T'
          or enlace = '97100153T'
          or enlace = '97100154T'
          or probsummarym1.company like '%ALIMENTOS, S.A.%'
          or probsummarym1.company like '%CENTRAL DE ALIMENTOS, S.A.%'
          or probsummarym1.company like '%CERVECERIA CENTROAMERICANA,  S.A.%'
          or probsummarym1.company like '%CERVECERIA CENTROAMERICANA, S.A.%'
          or probsummarym1.company like '%CERVECERIA DEL SUR, S.A.%'
          or probsummarym1.company like '%COMERCIAL LOS HERMANOS S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA ALINOR S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA COBANERA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA HUEHUETECA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA IZABAL,S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA JUTIAPANECA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA LA CEIBA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA LA NUEVA S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA LOS ALTOS, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA LOS CIPRESES, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA MALACATAN, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA MARAVILLA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA MARQUENSE, S.,A.%'
          or probsummarym1.company like '%DISTRIBUIDORA MAZATECA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA PANAMERICANA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA QUICHE, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA SAGITARIO, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA SANTA LUCIA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA SANTA ROSA, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA SATURNO, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA SAUZALITO, S.A.%'
          or probsummarym1.company like '%DISTRIBUIDORA ULTRARAPIDA%'
          or probsummarym1.company like '%EMBOTELLADORES UNIDOS, S.A.%'
          or probsummarym1.company like '%FUNDACION CASTILLO CORDOVA%'
          or probsummarym1.company like '%INDUSTRIAS AGRICOLAS CENTRO AMERICANAS S.A.%'
          or probsummarym1.company like '%INVERSIONES CENTROAMERICANAS S.A.%'
          or probsummarym1.company like '%INVERSIONES CENTROAMERICANAS, S.A.%'
          or probsummarym1.company like '%INYECTORES DE PLASTICO, S.A.%'
          or probsummarym1.company like '%MADERAS DE CENTRO AMERICA S.A.%'
          or probsummarym1.company like '%PRONE, PROMOCIONES Y NEGOCIOS, S.A.%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
    -- FIN 7
{{* ********************************************************************* *}}
    -- COD 8
update p_service_m
   set
   id_interno = '8'
 where probsummarym1.company like '%CREDOMATIC%GUATEMALA%'
   and ID_SM not like '%XT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%CREDOMATIC%GUATEMALA%'
          or probsummarym2.TG_COMPANY_CNOC like '%CREDOMATIC%GUATEMALA%'
          or probsummarym1.brief_description like '%CREDOMATIC%GUATEMALA%'
          or probsummarym1.action like '%CREDOMATIC%GUATEMALA%'
          -- tg_enlace_destino like '%CREDOMATIC%GUATEMALA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
    -- FIN 8
{{* ********************************************************************* *}}
--- COD 9
update p_service_m
   set
   id_interno = '9'
 where probsummarym1.company like '%DISTRIBUIDORA ELECTRONICA%'
   and ID_SM not like '%XT';
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%DISTRIBUIDORA ELECTRONICA%'
          or probsummarym2.TG_COMPANY_CNOC like '%DISTRIBUIDORA ELECTRONICA%'
          or probsummarym1.brief_description like '%DISTRIBUIDORA ELECTRONICA%'
          or probsummarym1.action like '%DISTRIBUIDORA ELECTRONICA%'
          -- tg_enlace_destino like '%DISTRIBUIDORA ELECTRONICA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA' 
	--and ID_SM not like '%XT' 
   );		
{{* ********************************************************************* *}}
-- FIN 9


-- COD 10 FENACOAC, R.L. | COOPERATIVA DE AHORRO Y CREDITO INTEGRAL SAN JOSE OBRERO R.L. | COOPERATIVA INTEGRAL DE AHORRO Y CREDITO EMPRESARIAL SAN JUAN BAUTISTA | COOPERATIVA PARROQUIAL GUADALUPANA R.L.
update p_service_m
   set
   id_interno = '10'
 where ( codigo_probsummarym1.company like '%2374%'
    or codigo_probsummarym1.company like '%3224%'
    or codigo_probsummarym1.company like '%4154%'
    or codigo_probsummarym1.company like '%3676%'
    or codigo_probsummarym1.company like '%2687%'
    or codigo_probsummarym1.company like '%FENACOAC%'
    or codigo_probsummarym1.company like '%COOPERATIVA DE AHORRO Y CREDITO INTEGRAL SAN JOSE OBRERO%'
    or codigo_probsummarym1.company like '%COOPERATIVA PARROQUIAL GUADALUPANA R.L%'
    or codigo_probsummarym1.company like '%COOPERATIVA INTEGRAL DE AHORRO Y CREDITO EMPRESARIAL SAN JUAN BAUTISTA%'
    or codigo_probsummarym1.company like '%COOPERATIVA PARROQUIAL GUADALUPANA R.L%'
    or codigo_probsummarym1.company like '%3438%' )
   and ID_SM not like '%XT';


 
        from t_tickets_cerrados_cnoc_lite
       where ( ( t_tickets_cerrados_cnoc_lite.customer_no = '2374'
          or  probsummarym1.company like '%FENACOAC%'
          or  probsummarym1.company like '%COOPERATIVA DE AHORRO Y CREDITO INTEGRAL SAN JOSE OBRERO%'
          or  probsummarym1.company like '%COOPERATIVA INTEGRAL DE AHORRO Y CREDITO EMPRESARIAL SAN JUAN BAUTISTA%'
          or  probsummarym1.company like '%COOPERATIVA PARROQUIAL GUADALUPANA%'
          or t_tickets_cerrados_cnoc_lite.customer_no = '3224'
          or t_tickets_cerrados_cnoc_lite.customer_no = '4154'
          or t_tickets_cerrados_cnoc_lite.customer_no = '3676'
          or t_tickets_cerrados_cnoc_lite.customer_no = '2687'
          or t_tickets_cerrados_cnoc_lite.customer_no = '3438'
          or tg_enlace like '%CC\_COOP\_SALCAJA\_GT%' escape '\' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA' 
	--and ID_SM not like '%XT' 
   );
{{* ********************************************************************* *}}
    -- FIN 10

-- COD 11
 update p_service_m
   set
   id_interno = '11'
 where probsummarym1.company like '%FUNDACION GENESIS EMPRESARIAL%'
   and ID_SM not like '%XT ';

    
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FUNDACION GENESIS EMPRESARIAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%FUNDACION GENESIS EMPRESARIAL%'
          or probsummarym1.brief_description like '%FUNDACION GENESIS EMPRESARIALA%'
          or probsummarym1.action like '%FUNDACION GENESIS EMPRESARIAL%'
          -- tg_enlace_destino like '%FUNDACION GENESIS EMPRESARIAL%'
          or tg_enlace like '%CC\_FUNDGENESIS\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA' 
	--and ID_SM not like '%XT' 
   );
{{* ********************************************************************* *}}
    -- FIN 11

-- COD 73
update p_service_m
   set
   id_interno = '73'
 where ( probsummarym1.company like '%GMG%'
    or probsummarym1.company like '%GRUPO%MONGE%'
    or probsummarym1.company like '%GALLO%MAS%GALLO%' )
    ;
 
 
           from t_tickets_cerrados_cnoc_lite
          where ( ( probsummarym1.company like '%CALLEJA%S.A.%'
             or probsummarym2.TG_COMPANY_CNOC like '%CALLEJA%S.A.%'
             or probsummarym1.brief_description like '%CALLEJA%S.A.%'
             or probsummarym1.action like '%CALLEJA%S.A.%'
             or tg_enlace like '%CC\_CALLEJA\_VIP %' escape '\' )
             or ( probsummarym1.company like '%GMG%EL%SALVADOR%S.A.%'
             or probsummarym2.TG_COMPANY_CNOC like '%GMG%EL%SALVADOR S.A.%'
             or probsummarym1.brief_description like '%GMG%EL%SALVADOR%S.A.%'
             or probsummarym1.action like '%GMG%EL%SALVADOR%S.A.%'
             or tg_enlace like '%CC\_GMG\_VIP %' escape '\' )
             or ( ( probsummarym1.company like '%GMG%COMERCIAL%HONDURAS%'
             or probsummarym1.company like '%GALLO%MAS%GALLO%' )
             or ( probsummarym2.TG_COMPANY_CNOC like '%GMG%COMERCIAL%HONDURAS%%'
             or probsummarym2.TG_COMPANY_CNOC like '%GALLO%MAS%GALLO%' )
             or ( probsummarym1.brief_description like '%GMG%COMERCIAL%HONDURAS%'
             or probsummarym1.brief_description like '%GALLO%MAS%GALLO%' )
             or ( probsummarym1.action like '%GMG%COMERCIAL%HONDURAS%'
             or probsummarym1.action like '%GALLO%MAS%GALLO%' ) )
             or ( ( probsummarym1.company like '%GMG%COMERCIAL%NICARAGUA%'
             or probsummarym1.company like '%GALLO%MAS%GALLO%' )
             or ( probsummarym2.TG_COMPANY_CNOC like '%GMG%COMERCIAL%NICARAGUA%%'
             or probsummarym2.TG_COMPANY_CNOC like '%GALLO%MAS%GALLO%' )
             or ( probsummarym1.brief_description like '%GMG%COMERCIAL%NICARAGUA%'
             or probsummarym1.brief_description like '%GALLO%MAS%GALLO%' )
             or ( probsummarym1.action like '%GMG%COMERCIAL%NICARAGUA%'
             or probsummarym1.action like '%GALLO%MAS%GALLO%' ) )
             or (  probsummarym1.company like '%GMG COMERCIAL COSTA RICA%'
             or probsummarym2.TG_COMPANY_CNOC like '%GMG COMERCIAL COSTA RICA%'
             or probsummarym1.brief_description like '%GMG COMERCIAL COSTA RICA%'
             or probsummarym1.action like '%GMG COMERCIAL COSTA RICA%'
             or tg_enlace like '%CC\_GMG\_CR%' escape '\'
             or tg_enlace like '%CC\_GMG\_760596OC%' escape '\' )
             or (  probsummarym1.company like '%GMG%GUATEMALA%'
             or probsummarym2.TG_COMPANY_CNOC like '%GMG%GUATEMALA%'
             or probsummarym1.brief_description like '%GMG%GUATEMALA%'
             or probsummarym1.action like '%GMG%GUATEMALA%'
             or tg_enlace like '%CC\_GMG\_GT%' escape '\' ) )
            and ( to_date(to_char(
               t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
               'DD/MM/YYYY'
            ),
           'DD/MM/YYYY') >= '01/02/2026'
            and to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
        'DD/MM/YYYY') < '01/03/2026' )
            and ID_SM not like '%XT'
      )
   )
    where ( cliente not like '%AZTECA%' )
       or ( cliente not like '%OPERADORA%' )
       or ( cliente not like '%SONAGUERA%' );
   -- FIN 73
{{* ********************************************************************* *}}
   -- COD 13

   update p_service_m
   set
   id_interno = '13'
   where ( probsummarym1.company like '%HOTEL%CAMINO%REAL%'
    or probsummarym1.company like '%HOTEL%CAMINOREAL%' )
   and ID_SM not like '%XT';
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%HOTEL%CAMINO%REAL%'
          or  probsummarym1.company like '%HOTEL%CAMINOREAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%HOTEL%CAMINO%REAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%HOTEL%CAMINOREAL%'
          or probsummarym1.brief_description like '%HOTEL%CAMINO%REAL%'
          or probsummarym1.brief_description like '%HOTEL%CAMINOREAL%'
          or probsummarym1.action like '%HOTEL%CAMINO%REAL%'
          or probsummarym1.action like '%HOTEL%CAMINOREAL%'
          -- tg_enlace_destino like '%HOTEL%CAMINO%REAL%'
          -- tg_enlace_destino like '%HOTEL%CAMINOREAL%'
          or tg_enlace like '%CC\_HCAMINO\_REAL\_GT%' escape '\'
          or tg_enlace like '%CC\_HOTEL\_CAMINO\_TIKAL\_GT%' escape '\'
          or tg_enlace like '%CC\_HCAMINO\_REAL\_TIKAL\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
 
    -- FIN 13

    -- COD 14
update p_service_m
   set
   id_interno = '14'
 where probsummarym1.company like '%IGLESIA%DE%JESUCRISTO%SUD%'
   and ID_SM not like '%XT';
   -- 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%IGLESIA%DE%JESUCRISTO%SUD%'
          or probsummarym2.TG_COMPANY_CNOC like '%IGLESIA%DE%JESUCRISTO%SUD%'
          or probsummarym1.brief_description like '%IGLESIA%DE%JESUCRISTO%SUD%'
          or probsummarym1.action like '%IGLESIA%DE%JESUCRISTO%SUD%'
          -- tg_enlace_destino like '%IGLESIA%DE%JESUCRISTO%SUD%'
          or tg_enlace like '%CC\_JSUD\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
    -- FIN 14
{{* ********************************************************************* *}}
 
    -- COD 15
update p_service_m
   set
   id_interno = '15'
 where probsummarym1.company like '%INGENIO%MAGDALENA%'
   and ID_SM not like '%XT';

 
             "RANGO SOLUCION 2"
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%INGENIO%MAGDALENA%'
          or probsummarym2.TG_COMPANY_CNOC like '%INGENIO%MAGDALENA%'
          or probsummarym1.brief_description like '%INGENIO%MAGDALENA%'
          or probsummarym1.action like '%INGENIO%MAGDALENA%'
          -- tg_enlace_destino like '%INGENIO%MAGDALENA%'
          or tg_enlace like '%CC\_IMSA\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 15
 
update p_service_m
   set
   id_interno = '18'
 where ( probsummarym1.company like '%BANCO AGRICOLA%' );

 
             "RANGO SOLUCION 2"
        from t_tickets_cerrados_cnoc_lite
       where ( tg_enlace_destino like '%BANCO AGRICOLA%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO AGRICOLA%'
          or probsummarym1.brief_description like '%BANCO AGRICOLA%'
          or probsummarym1.action like '%BANCO AGRICOLA%'
          -- tg_enlace_destino like '%BANCO AGRICOLA%'
          or tg_enlace like '%CC\_BANCO\_AGRICOLA\_VIP %' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR' 
	--and ID_SM not like '%XT' 
   );
{{* ********************************************************************* *}}
-- FIN 18

-- COD 19
update p_service_m
   set
   id_interno = '19'
 where ( probsummarym1.company like '%BANCO%AZTECA%' )
   and tg_country_code = 'SV'
   and ID_SM not like '%XT';

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%BANCO%AZTECA%' 
		--OR probsummarym2.TG_COMPANY_CNOC LIKE '%BANCO%AZTECA%' 
          or probsummarym1.brief_description like '%BANCO%AZTECA%'
          or probsummarym1.action like '%BANCO%AZTECA%'
          -- tg_enlace_destino like '%BANCO%AZTECA%'
          or tg_enlace like '%CC\_BANCO\_AZTECA\_VIP %' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
         and ID_SM not like '%XT'
   );
    -- FIN 19
{{* ********************************************************************* *}}
    -- COD 20

update p_service_m
   set
   id_interno = '20'
 where ( probsummarym1.company like '%CALLEJA S.A.%' )
   and ID_SM not like '%XT';

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%CALLEJA S.A.%'
          or probsummarym2.TG_COMPANY_CNOC like '%CALLEJA S.A.%'
          or probsummarym1.brief_description like '%CALLEJA S.A.%'
          or probsummarym1.action like '%CALLEJA S.A.%'
          -- tg_enlace_destino like '%CALLEJA S.A.%'
          or tg_enlace like '%CC\_CALLEJA\_VIP %' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 20

    -- COD 21
update p_service_m
      set
      id_interno = '21'
   where ( probsummarym1.company like '%GMG%EL%SALVADOR%S.A.%' )
   ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%GMG%EL%SALVADOR%S.A.%'
          or probsummarym2.TG_COMPANY_CNOC like '%GMG%EL%SALVADOR S.A.%'
          or probsummarym1.brief_description like '%GMG%EL%SALVADOR%S.A.%'
          or probsummarym1.action like '%GMG%EL%SALVADOR%S.A.%'
          -- tg_enlace_destino like '%GMG%EL%SALVADOR%S.A.%'
          or tg_enlace like '%CC\_GMG\_VIP %' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
         and ID_SM not like '%XT'
   );
    -- FIN 21
{{* ********************************************************************* *}}
    -- COD 22

update p_service_m
   set
   id_interno = '22'
 where ( probsummarym1.company like '%MINISTERIO DE HACIENDA%' )
   and tg_country_code = 'SV'
   and ID_SM not like '%XT';

    
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%MINISTERIO DE HACIENDA%' 
		--OR probsummarym2.TG_COMPANY_CNOC LIKE '%MINISTERIO DE HACIENDA%' 
          or probsummarym1.brief_description like '%MINISTERIO DE HACIENDA%'
          or probsummarym1.action like '%MINISTERIO DE HACIENDA%'
          -- tg_enlace_destino like '%MINISTERIO DE HACIENDA%'
          or tg_enlace like '%CC\_DGA\_VIP%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR' 
	--and ID_SM not like '%XT' 
   );
{{* ********************************************************************* *}}
    -- FIN 22

    -- COD 23
	/* DUPLICADO REUTILIZAR */
/*
    UPDATE P_SERVICE_M SET ID_INTERNO='23'    
WHERE
(probsummarym1.company like '%OMNISPORT%')
AND            
ENLACE NOT LIKE '%XT';

INSERT INTO TICKETS_2 (
			"TICKET",
			"ENLACE",
			"UBICACION",
			"PAIS",
			"MES CIERRE",
			"TG_COMPANY_CNOC",
			"CLIENTE",
			"PROBLEMA REPORTADO",
			"DETALLE PROBLEMA REPORTADO",
			"FALLA",
			"SUBFALLA",
			"SUB SUBFALLA",
			"ATRIBUIBLE A",
			"T TICKET ACTIVO (horas)",
			"FECHA DE CIERRE",
			"CODIGO DE CIERRE",
			"PROBLEM_TYPE",
			"RANGO SOLUCION",
			"RANGO SOLUCION 2",
			"DURACION TICKET (horas)",
			"TIPO MONITOREO",
			"SERVICIO",
			ID_INTERNO 
		) SELECT
		"TICKET",
		"ENLACE",
		"UBICACION",
		"PAIS",
		"MES CIERRE",
		"TG_COMPANY_CNOC",
		"CLIENTE",
		"PROBLEMA REPORTADO",
		"DETALLE PROBLEMA REPORTADO",
		"FALLA",
		"SUBFALLA",
		"SUB SUBFALLA",
		"ATRIBUIBLE A",
		"T TICKET ACTIVO (horas)",
		"FECHA DE CIERRE",
		"CODIGO DE CIERRE",
		"PROBLEM_TYPE",
		"RANGO SOLUCION",
		"RANGO SOLUCION 2",
		"DURACION TICKET (horas)",
		"TIPO MONITOREO",
		"SERVICIO",
		'23' AS ID_INTERNO 
	FROM
		(
		SELECT
			"TICKET",
			"ENLACE",
			"UBICACION",
			"PAIS",
			"MES CIERRE",
			"TG_COMPANY_CNOC",
			"CLIENTE",
			"PROBLEMA REPORTADO",
			"DETALLE PROBLEMA REPORTADO",
			"FALLA",
			"SUBFALLA",
			"SUB SUBFALLA",
			"ATRIBUIBLE A",
			 "T TICKET ACTIVO (horas)",
			"FECHA DE CIERRE",
			"CODIGO DE CIERRE",
			"PROBLEM_TYPE",
			"SERVICIO",
		  "RANGO SOLUCION",
            "DURACION TICKET (horas)",
            "TIPO MONITOREO",
            "RANGO SOLUCION 2"

FROM
	t_tickets_cerrados_cnoc_lite 
WHERE
	(
		probsummarym1.company like '%OMNISPORT%' 
		OR probsummarym2.TG_COMPANY_CNOC LIKE '%OMNISPORT%' 
		OR probsummarym1.brief_description LIKE '%OMNISPORT%' 
		OR probsummarym1.action LIKE '%OMNISPORT%' 
		-- tg_enlace_destino LIKE '%OMNISPORT%' 
		OR tg_enlace LIKE '%CC\_OMNISPORT\_VIP%' ESCAPE '\' 
	) 
	AND (
		TO_DATE( TO_CHAR( t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE", 'DD/MM/YYYY' ), 'DD/MM/YYYY' ) >= '01/02/2026'
		AND TO_DATE( TO_CHAR( t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE", 'DD/MM/YYYY' ), 'DD/MM/YYYY' ) < '01/03/2026' 
	) 
	AND PAIS = 'EL SALVADOR' 
	and ID_SM not like '%XT' 
	);

    -- FIN 23*/

    -- COD 24

update p_service_m
   set
   id_interno = '24'
 where ( probsummarym1.company like '%SOCIEDAD%DE%AHORRO%Y%CREDITO%APOYO%INTEGRAL%' )
   and ID_SM not like '%XT';

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%SOCIEDAD%DE%AHORRO%Y%CREDITO%APOYO%INTEGRAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%SOCIEDAD%DE%AHORRO%Y%CREDITO%APOYO%INTEGRAL%'
          or probsummarym1.brief_description like '%SOCIEDAD%DE%AHORRO%Y%CREDITO%APOYO%INTEGRAL%'
          or probsummarym1.action like '%SOCIEDAD%DE%AHORRO%Y%CREDITO%APOYO%INTEGRAL%'
          -- tg_enlace_destino like '%SOCIEDAD%DE%AHORRO%Y%CREDITO%APOYO%INTEGRAL%'
          or tg_enlace like '%CC\_APOYO\_VIP%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR' 
	-- ENLACE NOT LIKE '%XT' 
   );
{{* ********************************************************************* *}}
-- FIN 24

-- COD 25
update p_service_m
   set
   id_interno = '25'
 where ( probsummarym1.company like 'TACA%' )
   and ID_SM not like '%XT';
 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like 'TACA%'
          or probsummarym2.TG_COMPANY_CNOC like 'TACA%'
          or probsummarym1.brief_description like 'TACA%'
          or probsummarym1.action like 'TACA%'
          -- tg_enlace_destino like 'TACA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 25
-- COD 26

update p_service_m
   set
   id_interno = '26'
 where ( probsummarym1.company like '%AGROPECUARIA%MONTELIBANO%' );
 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%AGROPECUARIA%MONTELIBANO%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%AGROPECUARIA%MONTELIBANO%' )
          or ( probsummarym1.brief_description like '%MONTELIBANO%' )
          or ( probsummarym1.action like '%MONTELIBANO%' )
          or ( tg_enlace_destino like '%MONTELIBANO%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
    -- FIN 26
{{* ********************************************************************* *}}
    -- COD 27

update p_service_m
   set
   id_interno = '27'
 where tg_country_code = 'HN'
   and ( probsummarym1.company like '%BANRURAL%'
    or probsummarym1.company like '%BANCO%DE%DESAROLLO%RURAL%' );


 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%BANRURAL%'
          or probsummarym1.company like '%BANCO%DE%DESAROLLO%RURAL%HONDURAS%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANRURAL%'
          or probsummarym1.brief_description like '%BANRURAL%'
          or probsummarym1.action like '%BANRURAL%'
          -- tg_enlace_destino like '%BANRURAL%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
   );
{{* ********************************************************************* *}}
    -- FIN 27
    -- COD 28
update p_service_m
   set
   id_interno = '28'
 where ( probsummarym1.company like '%CADECA%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%CADECA%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%CADECA%' )
          or ( probsummarym1.brief_description like '%CADECA%' )
          or ( probsummarym1.action like '%CADECA%' )
          or ( tg_enlace_destino like '%CADECA%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
   );

    -- FIN 28
{{* ********************************************************************* *}}

    -- COD 29

update p_service_m
   set
   id_interno = '29'
 where ( probsummarym1.company like '%EMBOTELLADORA%LA%REYNA%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( ( ( probsummarym1.company like '%PEPSICO%'
          or probsummarym1.company like '%EMBOTELLADORA%LA%REYNA%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%PEPSICO%'
          or probsummarym2.TG_COMPANY_CNOC like '%EMBOTELLADORA%LA%REYNA%' )
          or ( probsummarym1.brief_description like '%PEPSICO%'
          or probsummarym1.brief_description like '%EMBOTELLADORA%LA%REYNA%' )
          or ( probsummarym1.action like '%PEPSICO%'
          or probsummarym1.action like '%EMBOTELLADORA%LA%REYNA%' )
          or ( tg_enlace_destino like '%PEPSICO%'
          -- tg_enlace_destino like '%EMBOTELLADORA%LA%REYNA%' ) )
         and ( cliente not like '%MOSANTO%AGRICOLA%HONDURAS%S.A.%'
         and cliente not like '%BOQUITAS%FIESTAS%S%DE%R%L%BOQUITAS%FIESTAS%S%DE%R%L%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );

    -- FIN 29
{{* ********************************************************************* *}}

    -- COD 30
update p_service_m
   set
   id_interno = '30'
 where ( probsummarym1.company like '%FUNDACION%MICROFINANCIERA%HERMANDAD%DE%HONDURAS%' );
 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%FUNDACION%MICROFINANCIERA%HERMANDAD%DE%HONDURAS%'
          or probsummarym2.TG_COMPANY_CNOC like '%FUNDACION%MICROFINANCIERA%HERMANDAD%DE%HONDURAS%'
          or probsummarym1.brief_description like '%FUNDACION%MICROFINANCIERA%HERMANDAD%DE%HONDURAS%'
          or probsummarym1.action like '%FUNDACION%MICROFINANCIERA%HERMANDAD%DE%HONDURAS%'
          -- tg_enlace_destino like '%FUNDACION%MICROFINANCIERA%HERMANDAD%DE%HONDURAS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
 -- FIN 30

 -- COD 31

update p_service_m
   set
   id_interno = '31'
 where ( probsummarym1.company like '%GMG%COMERCIAL%HONDURAS%'
    or probsummarym1.company like '%GALLO%MAS%GALLO%' )
    ;
 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%GMG%COMERCIAL%HONDURAS%'
          or probsummarym1.company like '%GALLO%MAS%GALLO%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%GMG%COMERCIAL%HONDURAS%%'
          or probsummarym2.TG_COMPANY_CNOC like '%GALLO%MAS%GALLO%' )
          or ( probsummarym1.brief_description like '%GMG%COMERCIAL%HONDURAS%'
          or probsummarym1.brief_description like '%GALLO%MAS%GALLO%' )
          or ( probsummarym1.action like '%GMG%COMERCIAL%HONDURAS%'
          or probsummarym1.action like '%GALLO%MAS%GALLO%' )
          or ( tg_enlace_destino like '%GMG%COMERCIAL%HONDURAS%'
          -- tg_enlace_destino like '%GALLO%MAS%GALLO%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 31

    -- COD 32
update p_service_m
   set
   id_interno = '32'
 where ( probsummarym1.company like '%LA%ARMERIA%' )
 ;
 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%LA%ARMERIA%'
          or probsummarym2.TG_COMPANY_CNOC like '%LA%ARMERIA%'
          or probsummarym1.brief_description like '%LA%ARMERIA%'
          or probsummarym1.action like '%LA%ARMERIA%'
          -- tg_enlace_destino like '%LA%ARMERIA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 32

-- COD 33
update p_service_m
   set
   id_interno = '33'
 where ( probsummarym1.company like '%ODEF%FINANCIERA%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%ODEF%FINANCIERA%'
          or probsummarym2.TG_COMPANY_CNOC like '%ODEF%FINANCIERA%'
          or probsummarym1.brief_description like '%ODEF%FINANCIERA%'
          or probsummarym1.action like '%ODEF%FINANCIERA%'
          -- tg_enlace_destino like '%ODEF%FINANCIERA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
    -- FIN 33
{{* ********************************************************************* *}}
    -- COD 34
update p_service_m
   set
   id_interno = '34'
 where ( probsummarym1.company like '%SECRETARIA%DE%FINANZAS%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%SECRETARIA%DE%FINANZAS%'
          or probsummarym2.TG_COMPANY_CNOC like '%SECRETARIA%DE%FINANZAS%'
          or probsummarym1.brief_description like '%SECRETARIA%DE%FINANZAS%'
          or probsummarym1.action like '%SECRETARIA%DE%FINANZAS%'
          -- tg_enlace_destino like '%SECRETARIA%DE%FINANZAS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
-- FIN 34
{{* ********************************************************************* *}}
-- COD 35

update p_service_m
   set
   id_interno = '35'
 where ( probsummarym1.company like '%SUPER%FARMACIA%SIMAN%' )
 ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%SUPER%FARMACIA%SIMAN%'
          or probsummarym2.TG_COMPANY_CNOC like '%SUPER%FARMACIA%SIMAN%'
          or probsummarym1.brief_description like '%SUPER%FARMACIA%SIMAN%'
          or probsummarym1.action like '%SUPER%FARMACIA%SIMAN%'
          -- tg_enlace_destino like '%SUPER%FARMACIA%SIMAN%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    --FIN 35
    -- COD 36 

update p_service_m
   set
   id_interno = '36'
 where ( probsummarym1.company like '%BANCO%DE%AM�RICA%CENTRAL%'
    or probsummarym1.company like '%BANCO%AMERICA%CENTRAL%' )
    ;
 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%BANCO%DE%AM�RICA%CENTRAL%'
          or probsummarym1.company like '%BANCO%AMERICA%CENTRAL%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%BANCO%DE%AM�RICA%CENTRAL%%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO%AMERICA%CENTRAL%' )
          or ( probsummarym1.brief_description like '%BANCO%DE%AM�RICA%CENTRAL%'
          or probsummarym1.brief_description like '%BANCO%AMERICA%CENTRAL%' )
          or ( probsummarym1.action like '%BANCO%DE%AM�RICA%CENTRAL%'
          or probsummarym1.action like '%BANCO%AMERICA%CENTRAL%' )
          or ( tg_enlace_destino like '%BANCO%DE%AM�RICA%CENTRAL%'
          -- tg_enlace_destino like '%BANCO%AMERICA%CENTRAL%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA' 
	--and ID_SM not like '%XT' 
   );
{{* ********************************************************************* *}}
-- FIN 36

-- COD 37 
update p_service_m
   set
   id_interno = '37'
 where ( probsummarym1.company like '%BANCO%DE%FINANZAS%' ) ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%BANCO%DE%FINANZAS%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO%DE%FINANZAS%%'
          or probsummarym1.brief_description like '%BANCO%DE%FINANZAS%'
          or probsummarym1.action like '%BANCO%DE%FINANZAS%'
          -- tg_enlace_destino like '%BANCO%DE%FINANZAS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 37

-- COD 38

update p_service_m
   set
   id_interno = '38'
 where ( probsummarym1.company like '%B.A.N.P.R.O.%'
    or probsummarym1.company like '%BANCO DE LA PRODUCCION%' ) ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%B.A.N.P.R.O.%'
          or probsummarym1.company like '%BANCO DE LA PRODUCCION%' )
          or probsummarym2.TG_COMPANY_CNOC like '%B.A.N.P.R.O.%'
          or probsummarym1.brief_description like '%B.A.N.P.R.O.%'
          or probsummarym1.action like '%B.A.N.P.R.O.%'
          -- tg_enlace_destino like '%B.A.N.P.R.O.%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- fin 38

    -- COD 39

update p_service_m
   set
   id_interno = '39'
 where ( CLIENTE like '%BANCO%PROCREDIT%' ) ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%BANCO%PROCREDIT%' 
		--OR probsummarym2.TG_COMPANY_CNOC LIKE '%BANCO%PROCREDIT%%' 
          or probsummarym1.brief_description like '%BANCO%PROCREDIT%'
          or probsummarym1.action like '%BANCO%PROCREDIT%'
          -- tg_enlace_destino like '%BANCO%PROCREDIT%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 39
-- COD 40

update p_service_m
   set
   id_interno = '40'
 where ( CLIENTE like '%COMPA%CERVECERA%DE%NICARAGUA%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%COMPA%CERVECERA%DE%NICARAGUA%'
          or probsummarym2.TG_COMPANY_CNOC like '%COMPA%CERVECERA%DE%NICARAGUA%%'
          or probsummarym1.brief_description like '%COMPA%CERVECERA%DE%NICARAGUA%'
          or probsummarym1.action like '%COMPA%CERVECERA%DE%NICARAGUA%'
          -- tg_enlace_destino like '%COMPA%CERVECERA%DE%NICARAGUA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 40

-- COD 41

update p_service_m
   set
   id_interno = '41'
 where (CLIENTE like '%CONSEJO%SUPREMO%ELECTORAL%'
    or  CLIENTE like '%CSE' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%CONSEJO%SUPREMO%ELECTORAL%'
          or probsummarym1.company like '%CSE' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%CONSEJO%SUPREMO%ELECTORAL%%'
          or probsummarym2.TG_COMPANY_CNOC like '%CSE' )
          or ( probsummarym1.brief_description like '%CONSEJO%SUPREMO%ELECTORAL%'
          or probsummarym1.brief_description like '%CSE' )
          or ( probsummarym1.action like '%CONSEJO%SUPREMO%ELECTORAL%'
          or probsummarym1.action like '%CSE' )
          or ( tg_enlace_destino like '%CONSEJO%SUPREMO%ELECTORAL%'
          -- tg_enlace_destino like '%CSE' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
	-- FIN 41

    -- COD 42
/*update p_service_m
   set
   id_interno = '42'
 where ( probsummarym1.company like '%GMG%COMERCIAL%NICARAGUA%'
    or probsummarym1.company like '%GALLO%MAS%GALLO%' );

 insert into tickets_2 (
   "TICKET",
   "ENLACE",
   "UBICACION",
   "PAIS",
   "MES CIERRE",
   "TG_COMPANY_CNOC",
   "CLIENTE",
   "PROBLEMA REPORTADO",
   "DETALLE PROBLEMA REPORTADO",
   "FALLA",
   "SUBFALLA",
   "SUB SUBFALLA",
   "ATRIBUIBLE A",
   "T TICKET ACTIVO (horas)",
   "FECHA DE CIERRE",
   "CODIGO DE CIERRE",
   "PROBLEM_TYPE",
   "RANGO SOLUCION",
   "RANGO SOLUCION 2",
   "DURACION TICKET (horas)",
   "TIPO MONITOREO",
   "SERVICIO",
   id_interno
 )
   select "TICKET",
          "ENLACE",
          "UBICACION",
          "PAIS",
          "MES CIERRE",
          "TG_COMPANY_CNOC",
          "CLIENTE",
          substr(
             "PROBLEMA REPORTADO",
             1,
             3990
          ) "PROBLEMA REPORTADO",
          substr(
             "DETALLE PROBLEMA REPORTADO",
             1,
             3990
          ) "DETALLE PROBLEMA REPORTADO",
          "FALLA",
          "SUBFALLA",
          "SUB SUBFALLA",
          "ATRIBUIBLE A",
          "T TICKET ACTIVO (horas)",
          "FECHA DE CIERRE",
          "CODIGO DE CIERRE",
          "PROBLEM_TYPE",
          "RANGO SOLUCION",
          "RANGO SOLUCION 2",
          "DURACION TICKET (horas)",
          "TIPO MONITOREO",
          "SERVICIO",
          '42' as id_interno
     from (
      select "TICKET",
             "ENLACE",
             "UBICACION",
             "PAIS",
             "MES CIERRE",
             "TG_COMPANY_CNOC",
             "CLIENTE",
             "PROBLEMA REPORTADO",
             "DETALLE PROBLEMA REPORTADO",
             "FALLA",
             "SUBFALLA",
             "SUB SUBFALLA",
             "ATRIBUIBLE A",
             "T TICKET ACTIVO (horas)",
             "FECHA DE CIERRE",
             "CODIGO DE CIERRE",
             "PROBLEM_TYPE",
             "SERVICIO",
             "RANGO SOLUCION",
             "DURACION TICKET (horas)",
             "TIPO MONITOREO",
             "RANGO SOLUCION 2"
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%GMG%COMERCIAL%NICARAGUA%'
          or probsummarym1.company like '%GALLO%MAS%GALLO%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%GMG%COMERCIAL%NICARAGUA%%'
          or probsummarym2.TG_COMPANY_CNOC like '%GALLO%MAS%GALLO%' )
          or ( probsummarym1.brief_description like '%GMG%COMERCIAL%NICARAGUA%'
          or probsummarym1.brief_description like '%GALLO%MAS%GALLO%' )
          or ( probsummarym1.action like '%GMG%COMERCIAL%NICARAGUA%'
          or probsummarym1.action like '%GALLO%MAS%GALLO%' )
          or ( tg_enlace_destino like '%GMG%COMERCIAL%NICARAGUA%'
          -- tg_enlace_destino like '%GALLO%MAS%GALLO%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 42*/

-- COD 43
update p_service_m
   set
   id_interno = '43'
 where ( CLIENTE like '%MONTEROSA%'
      or CLIENTE like '%MONTE%ROSA%' ) ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( ( probsummarym1.company like '%MONTEROSA%'
          or probsummarym1.company like '%MONTE%ROSA%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%MONTEROSA%'
          or probsummarym2.TG_COMPANY_CNOC like '%MONTE%ROSA%' )
          or ( probsummarym1.brief_description like '%MONTEROSA%'
          or probsummarym1.brief_description like '%MONTERROSA%' )
          or ( probsummarym1.action like '%MONTEROSA%'
          or probsummarym1.action like '%MONTERROSA%' )
          or ( tg_enlace_destino like '%MONTEROSA%'
          -- tg_enlace_destino like '%MONTERROSA%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 43


    -- COD 44
update p_service_m
   set
   id_interno = '44'
 where ( probsummarym1.company like '%NICARAGUA%SUGAR%' ) ;
 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%NICARAGUA%SUGAR%(NSUGAR)%' 
		--OR probsummarym2.TG_COMPANY_CNOC LIKE '%NICARAGUA%SUGAR%(NSUGAR)%%' 
          or probsummarym1.brief_description like '%NICARAGUA%SUGAR%(NSUGAR)%'
          or probsummarym1.action like '%NICARAGUA%SUGAR%(NSUGAR)%'
          -- tg_enlace_destino like '%NICARAGUA%SUGAR%(NSUGAR)%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 44

    -- COD 45
update p_service_m
   set
   id_interno = '45'
 where (   CLIENTE like '%POLICIA%NACIONAL%'
      or   CLIENTE like '%APOYO%A%MEDIDAS%DE%PREVENCION%Y%CONTROL%' )
       ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( cliente not like ( '%INTA%' )
         and ( ( probsummarym1.company like '%POLICIA%NACIONAL%'
          or probsummarym1.company like '%APOYO%A%MEDIDAS%DE%PREVENCION%Y%CONTROL%' )
          or ( probsummarym2.TG_COMPANY_CNOC like '%POLICIA%NACIONAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%APOYO%A%MEDIDAS%DE%PREVENCION%Y%CONTROL%' )
          or ( probsummarym1.brief_description like '%POLICIA%NACIONAL%'
          or probsummarym1.brief_description like '%APOYO%A%MEDIDAS%DE%PREVENCION%Y%CONTROL%' )
          or ( probsummarym1.action like '%POLICIA%NACIONAL%'
          or probsummarym1.action like '%APOYO%A%MEDIDAS%DE%PREVENCION%Y%CONTROL%' )
          or ( tg_enlace_destino like '%POLICIA%NACIONAL%'
          -- tg_enlace_destino like '%APOYO%A%MEDIDAS%DE%PREVENCION%Y%CONTROL%' ) ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'NICARAGUA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
    -- FIN 45

    -- COD 46
/*
update p_service_m
   set
   id_interno = '46'
 where probsummarym1.company like '%GMG COMERCIAL COSTA RICA%'
   and ID_SM not like '%XT';

 insert into tickets_2 (
   "TICKET",
   "ENLACE",
   "UBICACION",
   "PAIS",
   "MES CIERRE",
   "TG_COMPANY_CNOC",
   "CLIENTE",
   "PROBLEMA REPORTADO",
   "DETALLE PROBLEMA REPORTADO",
   "FALLA",
   "SUBFALLA",
   "SUB SUBFALLA",
   "ATRIBUIBLE A",
   "T TICKET ACTIVO (horas)",
   "FECHA DE CIERRE",
   "CODIGO DE CIERRE",
   "PROBLEM_TYPE",
   "RANGO SOLUCION",
   "RANGO SOLUCION 2",
   "DURACION TICKET (horas)",
   "TIPO MONITOREO",
   "SERVICIO",
   id_interno
 )
   select "TICKET",
          "ENLACE",
          "UBICACION",
          "PAIS",
          "MES CIERRE",
          "TG_COMPANY_CNOC",
          "CLIENTE",
          substr(
             "PROBLEMA REPORTADO",
             1,
             3990
          ) "PROBLEMA REPORTADO",
          substr(
             "DETALLE PROBLEMA REPORTADO",
             1,
             3990
          ) "DETALLE PROBLEMA REPORTADO",
          "FALLA",
          "SUBFALLA",
          "SUB SUBFALLA",
          "ATRIBUIBLE A",
          "T TICKET ACTIVO (horas)",
          "FECHA DE CIERRE",
          "CODIGO DE CIERRE",
          "PROBLEM_TYPE",
          "RANGO SOLUCION",
          "RANGO SOLUCION 2",
          "DURACION TICKET (horas)",
          "TIPO MONITOREO",
          "SERVICIO",
          '46' as id_interno
     from (
      select "TICKET",
             "ENLACE",
             "UBICACION",
             "PAIS",
             "MES CIERRE",
             "TG_COMPANY_CNOC",
             "CLIENTE",
             "PROBLEMA REPORTADO",
             "DETALLE PROBLEMA REPORTADO",
             "FALLA",
             "SUBFALLA",
             "SUB SUBFALLA",
             "ATRIBUIBLE A",
             "T TICKET ACTIVO (horas)",
             "FECHA DE CIERRE",
             "CODIGO DE CIERRE",
             "PROBLEM_TYPE",
             "SERVICIO",
             "RANGO SOLUCION",
             "DURACION TICKET (horas)",
             "TIPO MONITOREO",
             "RANGO SOLUCION 2"
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%GMG COMERCIAL COSTA RICA%'
          or probsummarym2.TG_COMPANY_CNOC like '%GMG COMERCIAL COSTA RICA%'
          or probsummarym1.brief_description like '%GMG COMERCIAL COSTA RICA%'
          or probsummarym1.action like '%GMG COMERCIAL COSTA RICA%'
          -- tg_enlace_destino like '%GMG COMERCIAL COSTA RICA%'
          or tg_enlace like '%CC\_GMG\_CR%' escape '\'
          or tg_enlace like '%CC\_GMG\_760596OC%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'COSTA RICA'
         and ID_SM not like '%XT'
   );
*/
{{* ********************************************************************* *}}
-- FIN 46


-- COD 47
update p_service_m
   set
   id_interno = '47'
 where ( ( CLIENTE like '%OPERADORA%DE%TIENDAS%'
        or CLIENTE like '%OPERADORA%DEL%SUR%'
        or CLIENTE like '%OPERADORA%DE%ORIENTE%'
        or CLIENTE like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
        or CLIENTE like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SRL%'
        or CLIENTE like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%DE%RESPONSABILIDAD%LIMITADA%' 
        )
   and ID_SM not like 'XT %' );

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%OPERADORA DE TIENDAS%'
          or probsummarym2.TG_COMPANY_CNOC like '%OPERADORA DE TIENDAS%'
          or probsummarym1.brief_description like '%OPERADORA DE TIENDAS%'
          or probsummarym1.action like '%OPERADORA DE TIENDAS%'
          -- tg_enlace_destino like '%OPERADORA DE TIENDAS%'
          or tg_enlace like '%CC\_WALMART\_GT%' escape '\'
          or  probsummarym1.company like '%OPERADORA%DEL%SUR%'
          or probsummarym2.TG_COMPANY_CNOC like '%OPERADORA%DEL%SUR%'
          or probsummarym1.brief_description like '%OPERADORA%DEL%SUR%'
          or probsummarym1.action like '%OPERADORA%DEL%SUR%'
          -- tg_enlace_destino like '%OPERADORA%DEL%SUR%'
          or  probsummarym1.company like '%OPERADORA%DE%ORIENTE%'
          or probsummarym2.TG_COMPANY_CNOC like '%OPERADORA%DE%ORIENTE%'
          or probsummarym1.brief_description like '%OPERADORA%DE%ORIENTE%'
          or probsummarym1.action like '%OPERADORA%DE%ORIENTE%'
          -- tg_enlace_destino like '%OPERADORA%DE%ORIENTE%'
          or  probsummarym1.company like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or probsummarym1.brief_description like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or probsummarym1.action like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          -- tg_enlace_destino like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or  probsummarym1.company like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or probsummarym1.brief_description like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or probsummarym1.action like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          -- tg_enlace_destino like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%'
          or  probsummarym1.company like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%ANONIMA%'
          or probsummarym2.TG_COMPANY_CNOC like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%ANONIMA%'
          or probsummarym1.brief_description like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%ANONIMA%'
          or probsummarym1.action like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%ANONIMA%'
          -- tg_enlace_destino like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%ANONIMA%'
          or  probsummarym1.company like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%DE%RESPONSABILIDAD%LIMITADA%'
          or probsummarym2.TG_COMPANY_CNOC like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%DE%RESPONSABILIDAD%LIMITADA%'
          or probsummarym1.brief_description like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%DE%RESPONSABILIDAD%LIMITADA%'
          or probsummarym1.action like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%DE%RESPONSABILIDAD%LIMITADA%'
          -- tg_enlace_destino like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SOCIEDAD%DE%RESPONSABILIDAD%LIMITADA%'
          or  probsummarym1.company like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SRL%'
          or probsummarym2.TG_COMPANY_CNOC like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SRL%'
          or probsummarym1.brief_description like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SRL%'
          or probsummarym1.action like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SRL%'
          -- tg_enlace_destino like '%CORPORACION%DE%SUPERMERCADOS%UNIDOS%SRL%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and ( pais = 'GUATEMALA'
          or pais = 'EL SALVADOR'
          or pais = 'HONDURAS'
          or pais = 'NICARAGUA'
          or pais = 'COSTA RICA' )
   );
{{* ********************************************************************* *}}
-- FIN 47


-- COD 48
update p_service_m
   set
   id_interno = '48'
 where CLIENTE like 'UNION%COMERCIA%DE%GUATEMALA%S.A.%'
    or CLIENTE like '%UNION%COMERCIAL%DE%GUATEMALA%SOCIEDAD%ANONIMA%'
   and ID_SM not like '%XT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like 'UNION%COMERCIA%DE%GUATEMALA%S.A.%'
          or  probsummarym1.company like '%UNION%COMERCIAL%GUATEMALA%SOCIEDAD%ANONIMA%'
          or probsummarym2.TG_COMPANY_CNOC like 'UNION%COMERCIA%DE%GUATEMALA%S.A.%'
          or probsummarym2.TG_COMPANY_CNOC like '%UNION%COMERCIAL%GUATEMALA%SOCIEDAD%ANONIMA%'
          or probsummarym1.brief_description like 'UNION%COMERCIA%DE%GUATEMALA%S.A.%'
          or probsummarym1.brief_description like '%UNION%COMERCIAL%GUATEMALA%SOCIEDAD%ANONIMA%'
          or probsummarym1.action like 'UNION%COMERCIA%DE%GUATEMALA%S.A.%'
          or probsummarym1.action like '%UNION%COMERCIAL%GUATEMALA%SOCIEDAD%ANONIMA%'
          -- tg_enlace_destino like 'UNION%COMERCIA%DE%GUATEMALA%S.A.%'
          -- tg_enlace_destino like '%UNION%COMERCIAL%GUATEMALA%SOCIEDAD%ANONIMA%'  

    -- tg_enlace LIKE '%CC\UNICOMER\VIP%' ESCAPE '\'
           )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 48


-- COD 49
update p_service_m
   set
   id_interno = '49'
 where ( CLIENTE like '%ADMINISTRACION%DE%CALL%CENTERS%SA%CV'
      or CLIENTE like '%OH1000604243%' ) ;


        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%ADMINISTRACION%DE%CALL%CENTERS%SA%CV'
          or probsummarym1.company like '%OH1000604243%'
          or probsummarym2.TG_COMPANY_CNOC like '%ADMINISTRACION%DE%CALL%CENTERS%SA%CV'
          or probsummarym2.TG_COMPANY_CNOC like '%OH1000604243%'
          or probsummarym1.brief_description like '%ADMINISTRACION%DE%CALL%CENTERS%SA%CV'
          or probsummarym1.brief_description like '%OH1000604243%'
          -- tg_enlace_destino like '%ADMINISTRACION%DE%CALL%CENTERS%SA%CV'
          -- tg_enlace_destino like '%OH1000604243%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 49

-- COD 50
update p_service_m
   set
   id_interno = '50'
 where ( CLIENTE like '%COLUMBUS%NETWORKS%HONDURAS'
      or CLIENTE like '%OH1000005886%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%COLUMBUS%NETWORKS%HONDURAS'
          or probsummarym1.company like '%OH1000005886%'
          or probsummarym2.TG_COMPANY_CNOC like '%COLUMBUS%NETWORKS%HONDURAS'
          or probsummarym2.TG_COMPANY_CNOC like '%OH1000005886%'
          or probsummarym1.brief_description like '%COLUMBUS%NETWORKS%HONDURAS'
          or probsummarym1.brief_description like '%OH1000005886%'
          or probsummarym1.action like '%COLUMBUS%NETWORKS%HONDURAS'
          or probsummarym1.action like '%OH1000005886%'
          -- tg_enlace_destino like '%COLUMBUS%NETWORKS%HONDURAS'
          -- tg_enlace_destino like '%OH1000005886%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 50

-- COD 51
update p_service_m
   set
   id_interno = '51'
 where ( CLIENTE like '%EXPORTADORA%ATLANTICO%'
      or CLIENTE like '%OH1000519184%' );

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%OH1000519184%'
          or probsummarym1.company like '%EXPORTADORA%ATLANTICO%'
          or probsummarym2.TG_COMPANY_CNOC like '%EXPORTADORA%ATLANTICO%'
          or probsummarym1.brief_description like '%EXPORTADORA%ATLANTICO%'
          or probsummarym1.brief_description like '%OH1000519184%'
          or probsummarym1.action like '%EXPORTADORA%ATLANTICO'
          or probsummarym1.action like '%OH1000519184'
          -- tg_enlace_destino like '%OH1000519184/EXPORTADORA%ATLANTICO%'
          -- tg_enlace_destino like '%EXPORTADORA%ATLANTICO%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 51

-- COD 52
update p_service_m
   set
   id_interno = '52'
 where ( CLIENTE like '%BANCO%CENTROAMERICANO%INTEGRACION%ECONOMICA%' )
    or ( CLIENTE like '%BCIE%' )
    or ( CLIENTE like '%B.C.I.E%' ) ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%BANCO%CENTROAMERICANO%INTEGRACION%ECONOMICA%' )
          or ( probsummarym1.company like '%BCIE%' )
          or ( probsummarym1.company like '%B.C.I.E%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO%CENTROAMERICANO%INTEGRACION%ECONOMICA%'
          or probsummarym2.TG_COMPANY_CNOC like '%B.C.I.E%'
          or probsummarym1.brief_description like '%BANCO%CENTROAMERICANO%INTEGRACION%ECONOMICA%'
          or probsummarym1.brief_description like '%BCIE%'
          or probsummarym1.brief_description like '%B.C.I.E%'
          or probsummarym1.action like '%BANCO%CENTROAMERICANO%INTEGRACION%ECONOMICA%'
          or probsummarym1.action like '%BCIE%'
          or probsummarym1.action like '%B.C.I.E%'
          or tg_enlace_destino like '%BANCO%CENTROAMERICANO%INTEGRACION%ECONOMICA%'
          or tg_enlace_destino like '%BCIE%'
          or tg_enlace_destino like '%B.C.I.E%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 52

-- COD 53
update p_service_m
   set
   id_interno = '53'
   where ( CLIENTE like '%INGENIERIA%GERENCIAL%'
        or CLIENTE like '%OH1000702486%' )
    ;


        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%INGENIERIA%GERENCIAL%'
          or probsummarym1.company like '%OH1000702486%'
          or --probsummarym2.TG_COMPANY_CNOC LIKE  '%INGENIERIA%GERENCIAL%' 
          or probsummarym1.brief_description like '%EXPORTADORA%ATLANTICO%'
          or probsummarym1.brief_description like '%OH1000702486%'
          or probsummarym1.action like '%INGENIERIA%GERENCIAL%'
          or probsummarym1.action like '%OH1000702486'
          or tg_enlace_destino like '%INGENIERIA%GERENCIAL%'
          or tg_enlace_destino like '%OH1000702486%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 53

-- COD 54
update p_service_m
   set
   id_interno = '54'
 where ( CLIENTE like '%TRIBUNAL%SUPREMO%ELECTORAL%'
      or CLIENTE like '%OH1000638985%' );


        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym1.company like '%OH1000638985%'
          or probsummarym2.TG_COMPANY_CNOC like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym1.brief_description like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym1.brief_description like '%OH1000638985%'
          or probsummarym1.action like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym1.action like '%OH1000638985%'
          -- tg_enlace_destino like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          -- tg_enlace_destino like '%OH1000638985%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 54

-- COD 55
update p_service_m
   set
   id_interno = '55'
 where probsummarym1.company like '%ACEROS%DE%GUATEMALA%' ;

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%ACEROS DE GUATEMALA%'
          or probsummarym2.TG_COMPANY_CNOC like '%ACEROS DE GUATEMALA%'
          or probsummarym1.brief_description like '%ACEROS DE GUATEMALA%'
          or probsummarym1.action like '%ACEROS DE GUATEMALA%'
          -- tg_enlace_destino like '%ACEROS DE GUATEMALA%'
          or tg_enlace like '%CC\_ACEROS DE GUATEMALA\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}
    -- FIN 55

    -- COD 56
update p_service_m
   set
   id_interno = '56'
 where probsummarym1.company like '%BANCO%DE%ANTIGUA%' ;

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BANCO DE ANTIGUA%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO DE ANTIGUA%'
          or probsummarym1.brief_description like '%BANCO DE ANTIGUA%'
          or probsummarym1.action like '%BANCO DE ANTIGUA%'
          -- tg_enlace_destino like '%BANCO DE ANTIGUA%'
          or tg_enlace like '%CC\_BANCO DE ANTIGUA\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}
    -- FIN 56

    -- COD 57
update p_service_m
   set
   id_interno = '57'
 where probsummarym1.company like '%AVICOLA%VILLALOBOS%'
 ;

 
        from t_tickets_cerrados_cnoc_lite
       where ( (  probsummarym1.company like '%AVICOLA VILLALOBOS%'
          or  probsummarym1.company like '%AVICOLA VILLALOBOS%' )
          or (  probsummarym1.company like '%AVICOLA VILLALOBOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%AVICOLA VILLALOBOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%AVICOLA VILLALOBOS%'
          or probsummarym1.brief_description like '%AVICOLA VILLALOBOS%'
          or probsummarym1.brief_description like '%AVICOLA VILLALOBOS%'
          or probsummarym1.action like '%AVICOLA VILLALOBOS%' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 57

-- COD 58
update p_service_m
   set
   id_interno = '58'
 where probsummarym1.company like '%PROMERICA%' ;

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%PROMERICA%'
          or probsummarym2.TG_COMPANY_CNOC like '%PROMERICA%'
          or probsummarym1.brief_description like '%PROMERICA%'
          or probsummarym1.action like '%PROMERICA%'
          -- tg_enlace_destino like '%PROMERICA%'
          or tg_enlace like '%CC\_PROMERICA\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= to_date('01/02/2026','DD/MM/YYYY')
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < to_date('01/03/2026','DD/MM/YYYY') )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}
-- FIN 58

-- COD 59
update p_service_m
   set
   id_interno = '59'
 where probsummarym1.company like '%AJEMAYA%'
 ;
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%AJEMAYA%'
          or probsummarym2.TG_COMPANY_CNOC like '%AJEMAYA%'
          or probsummarym1.brief_description like '%AJEMAYA%'
          or probsummarym1.action like '%AJEMAYA%'
          -- tg_enlace_destino like '%AJEMAYA%'
          or tg_enlace like '%CC\_%AJEMAYA%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}
-- FIN 59

-- COD 60
update p_service_m
   set
   id_interno = '60'
 where probsummarym1.company like '%BARISTA%'
 ;

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BARISTA%'
          or probsummarym2.TG_COMPANY_CNOC like '%BARISTA%'
          or probsummarym1.brief_description like '%BARISTA%'
          or probsummarym1.action like '%BARISTA%'
          -- tg_enlace_destino like '%BARISTA%'
          or tg_enlace like '%CC\_BARISTA\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}
-- FIN 60

-- COD 61
update p_service_m
   set
   id_interno = '61'
 where probsummarym1.company like '%CLOUD2NUBE%';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%CLOUD2NUBE%'
          or probsummarym2.TG_COMPANY_CNOC like '%CLOUD2NUBE%'
          or probsummarym1.brief_description like '%CLOUD2NUBE%'
          or probsummarym1.action like '%CLOUD2NUBE%'
          -- tg_enlace_destino like '%CLOUD2NUBE%'
          or tg_enlace like '%CC\_%CLOUD2NUBE%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}
-- FIN 61

-- COD 62
/*
   UPDATE P_SERVICE_M SET ID_INTERNO='62'     
   WHERE
   probsummarym1.company like '%POLLO%GRANJERO%' OR probsummarym1.company like '%PAPA%POLLO%';

   INSERT INTO TICKETS_2 ("TICKET",
   "ENLACE",
   "UBICACION",
   "PAIS", 
   "MES CIERRE",
   "TG_COMPANY_CNOC",
   "CLIENTE",
   "PROBLEMA REPORTADO",
   "DETALLE PROBLEMA REPORTADO",
   "FALLA",
   "SUBFALLA",
   "SUB SUBFALLA",
   "ATRIBUIBLE A", 
   "T TICKET ACTIVO (horas)" ,
   "FECHA DE CIERRE",
   "CODIGO DE CIERRE",
   "PROBLEM_TYPE",
      "RANGO SOLUCION",
      "RANGO SOLUCION 2",
      "DURACION TICKET (horas)",
      "TIPO MONITOREO",
      "SERVICIO",
      ID_INTERNO)

      SELECT 
      "TICKET",
      "ENLACE",
      "UBICACION",
   "PAIS", 
   "MES CIERRE",
   "TG_COMPANY_CNOC",
   "CLIENTE",
   "PROBLEMA REPORTADO",
   "DETALLE PROBLEMA REPORTADO",
   "FALLA",
   "SUBFALLA",
   "SUB SUBFALLA",
   "ATRIBUIBLE A", 
    "T TICKET ACTIVO (horas)" ,
    "FECHA DE CIERRE",
    "CODIGO DE CIERRE",
    "PROBLEM_TYPE",
   "RANGO SOLUCION",
   "RANGO SOLUCION 2",
   "DURACION TICKET (horas)",
   "TIPO MONITOREO",
   "SERVICIO",
   '62' AS ID_INTERNO
   FROM
(
    SELECT 

    "TICKET",
    "ENLACE",
    "UBICACION",
    "PAIS", 
    "MES CIERRE",
    "TG_COMPANY_CNOC",
    "CLIENTE",
    "PROBLEMA REPORTADO",
    "DETALLE PROBLEMA REPORTADO",
    "FALLA",
    "SUBFALLA",
    "SUB SUBFALLA",
    "ATRIBUIBLE A", 
     "T TICKET ACTIVO" *24 AS "T TICKET ACTIVO (horas)" ,
     "FECHA DE CIERRE",
     "CODIGO DE CIERRE",
     "PROBLEM_TYPE",
     "SERVICIO",
    "RANGO SOLUCION",
            "DURACION TICKET (horas)",
            "TIPO MONITOREO",
            "RANGO SOLUCION 2"

    FROM t_tickets_cerrados_cnoc_lite

   WHERE 
   (
      probsummarym1.company LIKE '%POLLO%GRANJERO%' OR 
     probsummarym2.TG_COMPANY_CNOC LIKE '%POLLO%GRANJERO%' OR
     probsummarym1.brief_description LIKE '%POLLO%GRANJERO%' OR
     probsummarym1.action LIKE '%POLLO%GRANJERO%' OR
     
     tg_enlace LIKE '%CC\_%POLLO%GRANJERO%\_GT%' ESCAPE '\'

   )
   OR 
    (
      probsummarym1.company LIKE '%PAPA%POLLO%' OR 
     probsummarym2.TG_COMPANY_CNOC LIKE '%PAPA%POLLO%' OR
     probsummarym1.brief_description LIKE '%PAPA%POLLO%' OR
     probsummarym1.action LIKE '%PAPA%POLLO%' OR
    
     tg_enlace LIKE '%CC\_%PAPA%POLLO%\_GT%' ESCAPE '\'

   )
   AND
   (
    TO_DATE( TO_CHAR( t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE", 'DD/MM/YYYY' ), 'DD/MM/YYYY' ) >= '01/02/2026'
		AND TO_DATE( TO_CHAR( t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE", 'DD/MM/YYYY' ), 'DD/MM/YYYY' ) < '01/03/2026' 
   )

   AND   
   PAIS = 'GUATEMALA' 
   );   */
{{* ********************************************************************* *}}
-- FIN 62

-- COD 63
update p_service_m
   set
   id_interno = '63'
 where probsummarym1.company like '%DISTRIBUIDORA%ME%LLEGA%';


        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%DISTRIBUIDORA%ME%LLEGA%'
          or probsummarym2.TG_COMPANY_CNOC like '%DISTRIBUIDORA%ME%LLEGA%'
          or probsummarym1.brief_description like '%DISTRIBUIDORA%ME%LLEGA%'
          or probsummarym1.action like '%DISTRIBUIDORA%ME%LLEGA%'
          -- tg_enlace_destino like '%DISTRIBUIDORA%ME%LLEGA%'
          or tg_enlace like '%CC\_%DISTRIBUIDORA%ME%LLEGA%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );      
{{* ********************************************************************* *}}
-- FIN 63

-- COD 64
update p_service_m
   set
   id_interno = '64'
 where probsummarym1.company like '%GLOBAL%CEMENT%';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%GLOBAL%CEMENT%'
          or probsummarym2.TG_COMPANY_CNOC like '%GLOBAL%CEMENT%'
          or probsummarym1.brief_description like '%GLOBAL%CEMENT%'
          or probsummarym1.action like '%GLOBAL%CEMENT%'
          -- tg_enlace_destino like '%GLOBAL%CEMENT%'
          or tg_enlace like '%CC\_%GLOBAL%CEMENT%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );        
{{* ********************************************************************* *}}
-- FIN 64

-- COD 65
update p_service_m
   set
   id_interno = '65'
 where probsummarym1.company like '%JAGUAR%ENERGY%';

        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%JAGUAR%ENERGY%'
          or probsummarym2.TG_COMPANY_CNOC like '%JAGUAR%ENERGY%'
          or probsummarym1.brief_description like '%JAGUAR%ENERGY%'
          or probsummarym1.action like '%JAGUAR%ENERGY%'
          -- tg_enlace_destino like '%JAGUAR%ENERGY%'
          or tg_enlace like '%CC\_%JAGUAR%ENERGY%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );  
{{* ********************************************************************* *}}         
-- FIN 65

-- COD 66
update p_service_m
   set
   id_interno = '66'
 where probsummarym1.company like '%MAPFRE%'
 ;

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%MAPFRE%'
          or probsummarym2.TG_COMPANY_CNOC like '%MAPFRE%'
          or probsummarym1.brief_description like '%MAPFRE%'
          or probsummarym1.action like '%MAPFRE%'
          -- tg_enlace_destino like '%MAPFRE%'
          or tg_enlace like '%CC\_%MAPFRE%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}  
-- FIN 66

-- COD 67
update p_service_m
   set
   id_interno = '67'
 where probsummarym1.company like '%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%'
 ;

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%'
          or probsummarym1.brief_description like '%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%'
          or probsummarym1.action like '%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%'
          -- tg_enlace_destino like '%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%'
          or tg_enlace like '%CC\_%PROCURADURIA%DE%LOS%DERECHOS%HUMANOS%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   ); 
{{* ********************************************************************* *}}    
-- FIN 67

-- COD 68
update p_service_m
   set
   id_interno = '68'
 where probsummarym1.company like '%TRIBUNAL%SUPREMO%ELECTORAL%';

        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym1.brief_description like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or probsummarym1.action like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          -- tg_enlace_destino like '%TRIBUNAL%SUPREMO%ELECTORAL%'
          or tg_enlace like '%CC\_%TRIBUNAL%SUPREMO%ELECTORAL%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );
{{* ********************************************************************* *}}   
-- FIN 68

-- COD 69
update p_service_m
   set
   id_interno = '69'
 where probsummarym1.company like '%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%';


        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%'
          or probsummarym2.TG_COMPANY_CNOC like '%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%'
          or probsummarym1.brief_description like '%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%'
          or probsummarym1.action like '%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%'
          -- tg_enlace_destino like '%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%'
          or tg_enlace like '%CC\_%UNIVERSIDAD%DA%VINCI%DE%GUATEMALA%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}   
-- FIN 69

-- COD 72
update p_service_m
   set
   id_interno = '72'
 where ( probsummarym1.company like '%OMNISPORT%' );


        from t_tickets_cerrados_cnoc_lite
       where ( probsummarym1.company like '%OMNISPORT%'
          or probsummarym2.TG_COMPANY_CNOC like '%OMNISPORT%'
          or probsummarym1.brief_description like '%OMNISPORT%'
          or probsummarym1.action like '%OMNISPORT%'
          -- tg_enlace_destino like '%OMNISPORT%'
          or tg_enlace like '%CC\_OMNISPORT\_VIP%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );
{{* ********************************************************************* *}} 
--FIN 72

-- COD 70
update p_service_m
   set
   id_interno = '70'
 where probsummarym1.company like '%UNISUPER%';


        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%UNISUPER%'
          or probsummarym2.TG_COMPANY_CNOC like '%UNISUPER%'
          or probsummarym1.brief_description like '%UNISUPER%'
          or probsummarym1.action like '%UNISUPER%'
          -- tg_enlace_destino like '%UNISUPER%'
          or tg_enlace like '%CC\_%UNISUPER%\_GT%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
   );    
{{* ********************************************************************* *}} 
-- FIN 70

-- COD 71
update p_service_m
   set
   id_interno = '71'
 where ( ( CLIENTE like '%APPLETOWN%SOCIEDAD%ANONIMA%'
        or CLIENTE like '%CONTROLES%GERENCIALES%'
        or CLIENTE like '%INDUSTRIA%DE%HAMBURGUESA%'
        or CLIENTE like '%INHARSA%'
        or CLIENTE like '%NATURE%TOWN%'
        or CLIENTE like '%ORIENTAL TOWN%' ) )
    ;

        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%APPLETOWN%SOCIEDAD%ANONIMA%'
          or probsummarym2.TG_COMPANY_CNOC like '%APPLETOWN%SOCIEDAD%ANONIMA%'
          or probsummarym1.brief_description like '%APPLETOWN%SOCIEDAD%ANONIMA%'
          or probsummarym1.action like '%APPLETOWN%SOCIEDAD%ANONIMA%'
          -- tg_enlace_destino like '%APPLETOWN%SOCIEDAD%ANONIMA%'
          or tg_enlace like '%CC\_%APPLETOWN%SOCIEDAD%ANONIMA%\_%' escape '\'
          or  probsummarym1.company like '%CONTROLES%GERENCIALES%'
          or probsummarym2.TG_COMPANY_CNOC like '%CONTROLES%GERENCIALES%'
          or probsummarym1.brief_description like '%CONTROLES%GERENCIALES%'
          or probsummarym1.action like '%CONTROLES%GERENCIALES%'
          -- tg_enlace_destino like '%CONTROLES%GERENCIALES%'
          or tg_enlace like '%CC\_%%CONTROLES%GERENCIALES%\_%' escape '\'
          or  probsummarym1.company like '%INDUSTRIA%DE%HAMBURGUESA%'
          or probsummarym2.TG_COMPANY_CNOC like '%INDUSTRIA%DE%HAMBURGUESA%'
          or probsummarym1.brief_description like '%INDUSTRIA%DE%HAMBURGUESA%'
          or probsummarym1.action like '%INDUSTRIA%DE%HAMBURGUESA%'
          -- tg_enlace_destino like '%INDUSTRIA%DE%HAMBURGUESA%'
          or tg_enlace like '%CC\_%INDUSTRIA%DE%HAMBURESA%\_%' escape '\'
          or  probsummarym1.company like '%INHARSA%'
          or probsummarym2.TG_COMPANY_CNOC like '%INHARSA%'
          or probsummarym1.brief_description like '%INHARSA%'
          or probsummarym1.action like '%INHARSA%'
          -- tg_enlace_destino like '%INHARSA%'
          or tg_enlace like '%CC\_%INHARSA%\_%' escape '\'
          or  probsummarym1.company like '%NATURE%TOWN%'
          or probsummarym2.TG_COMPANY_CNOC like '%NATURE%TOWN%'
          or probsummarym1.brief_description like '%NATURE%TOWN%'
          or probsummarym1.action like '%NATURE%TOWN%'
          -- tg_enlace_destino like '%NATURE%TOWN%'
          or tg_enlace like '%CC\_%NATURE%TOWN%\_%' escape '\'
          or  probsummarym1.company like '%ORIENTAL%TOWN%'
          or probsummarym2.TG_COMPANY_CNOC like '%ORIENTAL%TOWN%'
          or probsummarym1.brief_description like '%ORIENTAL%TOWN%'
          or probsummarym1.action like '%ORIENTAL%TOWN%'
          -- tg_enlace_destino like '%ORIENTAL%TOWN%'
          or tg_enlace like '%CC\_%ORIENTAL%TOWN%\_%' escape '\' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
   );
{{* ********************************************************************* *}} 
-- FIN 71

-- COD 74
update p_service_m
   set
   id_interno = '74'
 where probsummarym1.company like '%ALIMENTOS%PARA%ANIMALES%';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%ALIMENTOS%PARA%ANIMALES%'
          or probsummarym2.TG_COMPANY_CNOC like '%ALIMENTOS%PARA%ANIMALES%'
          or probsummarym1.brief_description like '%ALIMENTOS%PARA%ANIMALES%'
          or probsummarym1.action like '%ALIMENTOS%PARA%ANIMALES%'
          or tg_enlace like '%ALIMENTOS%PARA%ANIMALES%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   

{{* ********************************************************************* *}} 
-- FIN 74

-- COD 75
update p_service_m
   set
   id_interno = '75'
 where probsummarym1.company like '%CENTRO%DE%SERVICIOS%INTEGRADOS%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%CENTRO%DE%SERVICIOS%INTEGRADOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%CENTRO%DE%SERVICIOS%INTEGRADOS%'
          or probsummarym1.brief_description like '%CENTRO%DE%SERVICIOS%INTEGRADOS%'
          or probsummarym1.action like '%CENTRO%DE%SERVICIOS%INTEGRADOS%'
          or tg_enlace like '%CENTRO%DE%SERVICIOS%INTEGRADOS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   

{{* ********************************************************************* *}} 
-- FIN 75

-- COD 76
update p_service_m
   set
   id_interno = '76'
 where probsummarym1.company like '%CMI%ALIMENTOS%'
   and pais = 'GT';
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%CMI%ALIMENTOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%CMI%ALIMENTOS%'
          or probsummarym1.brief_description like '%CMI%ALIMENTOS%'
          or probsummarym1.action like '%CMI%ALIMENTOS%'
          or tg_enlace like '%CMI%ALIMENTOS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}} 
-- FIN 76

-- COD 77
update p_service_m
   set
   id_interno = '77'
 where probsummarym1.company like '%CMI%CAPITAL%'
   and pais = 'GT';

 
      from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%CMI%CAPITAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%CMI%CAPITAL%'
          or probsummarym1.brief_description like '%CMI%CAPITAL%'
          or probsummarym1.action like '%CMI%CAPITAL%'
          or tg_enlace like '%CMI%CAPITAL%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}} 
-- FIN 77
-- COD 78
update p_service_m
   set
   id_interno = '78'
 where probsummarym1.company like '%EMPACADORA%TOLEDO%'
   and pais = 'GT';
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%EMPACADORA%TOLEDO%'
          or probsummarym2.TG_COMPANY_CNOC like '%EMPACADORA%TOLEDO%'
          or probsummarym1.brief_description like '%EMPACADORA%TOLEDO%'
          or probsummarym1.action like '%EMPACADORA%TOLEDO%'
          or tg_enlace like '%EMPACADORA%TOLEDO%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 78
-- COD 79
update p_service_m
   set
   id_interno = '79'
 where probsummarym1.company like '%FIDEICOMISO%DE%ADMINISTRACION%PAGO%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FIDEICOMISO%DE%ADMINISTRACION%PAGO%'
          or probsummarym2.TG_COMPANY_CNOC like '%FIDEICOMISO%DE%ADMINISTRACION%PAGO%'
          or probsummarym1.brief_description like '%FIDEICOMISO%DE%ADMINISTRACION%PAGO%'
          or probsummarym1.action like '%FIDEICOMISO%DE%ADMINISTRACION%PAGO%'
          or tg_enlace like '%FIDEICOMISO%DE%ADMINISTRACION%PAGO%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 79

-- COD 80
update p_service_m
   set
   id_interno = '80'
 where probsummarym1.company like '%FINANCIERA%CONSOLIDADA%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FINANCIERA%CONSOLIDADA%'
          or probsummarym2.TG_COMPANY_CNOC like '%FINANCIERA%CONSOLIDADA%'
          or probsummarym1.brief_description like '%FINANCIERA%CONSOLIDADA%'
          or probsummarym1.action like '%FINANCIERA%CONSOLIDADA%'
          or tg_enlace like '%FINANCIERA%CONSOLIDADA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 80
-- COD 81
update p_service_m
   set
   id_interno = '81'
 where probsummarym1.company like '%FUNDACION%JUAN%BAUTISTA%GUTIERREZ%'
   and pais = 'GT';
 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FUNDACION%JUAN%BAUTISTA%GUTIERREZ%'
          or probsummarym2.TG_COMPANY_CNOC like '%FUNDACION%JUAN%BAUTISTA%GUTIERREZ%'
          or probsummarym1.brief_description like '%FUNDACION%JUAN%BAUTISTA%GUTIERREZ%'
          or probsummarym1.action like '%FUNDACION%JUAN%BAUTISTA%GUTIERREZ%'
          or tg_enlace like '%FUNDACION%JUAN%BAUTISTA%GUTIERREZ%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 81

-- COD 82
update p_service_m
   set
   id_interno = '82'
 where probsummarym1.company like '%INDUSTRIA%NACIONAL%ALIMENTICIA%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%INDUSTRIA%NACIONAL%ALIMENTICIA%'
          or probsummarym2.TG_COMPANY_CNOC like '%INDUSTRIA%NACIONAL%ALIMENTICIA%'
          or probsummarym1.brief_description like '%INDUSTRIA%NACIONAL%ALIMENTICIA%'
          or probsummarym1.action like '%INDUSTRIA%NACIONAL%ALIMENTICIA%'
          or tg_enlace like '%INDUSTRIA%NACIONAL%ALIMENTICIA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 82

-- COD 83
update p_service_m
   set
   id_interno = '83'
 where probsummarym1.company like '%INMOBILIARIA%PRADERA%XELA%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%INMOBILIARIA%PRADERA%XELA%'
          or probsummarym2.TG_COMPANY_CNOC like '%INMOBILIARIA%PRADERA%XELA%'
          or probsummarym1.brief_description like '%INMOBILIARIA%PRADERA%XELA%'
          or probsummarym1.action like '%INMOBILIARIA%PRADERA%XELA%'
          or tg_enlace like '%INMOBILIARIA%PRADERA%XELA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 83

-- COD 84
update p_service_m
   set
   id_interno = '84'
 where probsummarym1.company like '%INMOBILIARIA%VISTARES%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%INMOBILIARIA%VISTARES%'
          or probsummarym2.TG_COMPANY_CNOC like '%INMOBILIARIA%VISTARES%'
          or probsummarym1.brief_description like '%INMOBILIARIA%VISTARES%'
          or probsummarym1.action like '%INMOBILIARIA%VISTARES%'
          or tg_enlace like '%INMOBILIARIA%VISTARES%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 84

-- COD 89
update p_service_m
   set
   id_interno = '89'
 where probsummarym1.company like '%RENACE%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like 'RENACE%'
          or probsummarym2.TG_COMPANY_CNOC like 'RENACE%'
          or probsummarym1.brief_description like 'RENACE%'
          or probsummarym1.action like 'RENACE%'
          or tg_enlace like 'RENACE%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 89


-- COD 91
update p_service_m
   set
   id_interno = '91'
 where probsummarym1.company like '%SISTEMAS%Y%EQUIPOS%'
   and pais = 'GT';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%SISTEMAS%Y%EQUIPOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%SISTEMAS%Y%EQUIPOS%'
          or probsummarym1.brief_description like '%SISTEMAS%Y%EQUIPOS%'
          or probsummarym1.action like '%SISTEMAS%Y%EQUIPOS%'
          or tg_enlace like '%SISTEMAS%Y%EQUIPOS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 91  

-- COD 86
update p_service_m
   set
   id_interno = '86'
 where probsummarym1.company like '%MOLINOS%MODERNOS%'
   and pais = 'GT';
 

        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%MOLINOS%MODERNOS%'
          or probsummarym2.TG_COMPANY_CNOC like '%MOLINOS%MODERNOS%'
          or probsummarym1.brief_description like '%MOLINOS%MODERNOS%'
          or probsummarym1.action like '%MOLINOS%MODERNOS%'
          or tg_enlace like '%MOLINOS%MODERNOS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'GUATEMALA'
   );   
{{* ********************************************************************* *}}
-- FIN 86


-- COD 92
update p_service_m
   set
   id_interno = '92'
 where probsummarym1.company like '%MELHER%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%MELHER%'
          or probsummarym2.TG_COMPANY_CNOC like '%MELHER%'
          or probsummarym1.brief_description like '%MELHER%'
          or probsummarym1.action like '%MELHER%'
          or tg_enlace like '%MELHER%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 92

-- COD 93
update p_service_m
   set
   id_interno = '93'
 where ( cliente like '%ISSS%'
    or cliente = '%INSTITUTO SALVADORE_O DEL SEGURO SOCIAL%' )
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%ISSS%'
          or probsummarym2.TG_COMPANY_CNOC like '%ISSS%'
          or probsummarym1.brief_description like '%ISSS%'
          or probsummarym1.action like '%ISSS%'
          or  probsummarym1.company like '%INSTITUTO SALVADORE_O DEL SEGURO SOCIAL%'
          or probsummarym2.TG_COMPANY_CNOC like '%INSTITUTO SALVADORE_O DEL SEGURO SOCIAL%'
          or probsummarym1.brief_description like '%INSTITUTO SALVADORE_O DEL SEGURO SOCIAL%'
          or probsummarym1.action like '%INSTITUTO SALVADORE_O DEL SEGURO SOCIAL%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= to_date('01/02/2026','DD/MM/YYYY')
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < to_date('01/03/2026','DD/MM/YYYY') )
         and pais = 'EL SALVADOR'
   ) a
    where cliente not like 'COSTISSS DE R.L.'
       or tg_company_cnoc not like 'COSTISSS DE R.L.'
       or "PROBLEMA REPORTADO" not like 'COSTISSS DE R.L.'
       or "DETALLE PROBLEMA REPORTADO" not like 'COSTISSS DE R.L.';
  
{{* ********************************************************************* *}}
-- FIN 93

-- COD 94
update p_service_m
   set
   id_interno = '94'
 where probsummarym1.company like '%ENERGIA%DEL%PACIFICO%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%ENERGIA%DEL%PACIFICO%'
          or probsummarym2.TG_COMPANY_CNOC like '%ENERGIA%DEL%PACIFICO%'
          or probsummarym1.brief_description like '%ENERGIA%DEL%PACIFICO%'
          or probsummarym1.action like '%ENERGIA%DEL%PACIFICO%'
          or tg_enlace like '%ENERGIA%DEL%PACIFICO%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   ); 

{{* ********************************************************************* *}}
-- FIN 94

-- COD 95
update p_service_m
   set
   id_interno = '95'
 where probsummarym1.company like '%SERVICIOS%FINANCIEROS%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%SERVICIOS%FINANCIEROS%'
          or probsummarym2.TG_COMPANY_CNOC like '%SERVICIOS%FINANCIEROS%'
          or probsummarym1.brief_description like '%SERVICIOS%FINANCIEROS%'
          or probsummarym1.action like '%SERVICIOS%FINANCIEROS%'
          or tg_enlace like '%SERVICIOS%FINANCIEROS%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 95

-- COD 96
update p_service_m
   set
   id_interno = '96'
 where cliente like '%MULTIINVERSIONES_MIBANCO%'
    or cliente like '%BANCO%COOPERATIVO%DE%LOS%TRABAJADORES%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%MULTIINVERSIONES_MIBANCO%'
          or probsummarym2.TG_COMPANY_CNOC like '%MULTIINVERSIONES_MIBANCO%'
          or probsummarym1.brief_description like '%MULTIINVERSIONES_MIBANCO%'
          or probsummarym1.action like '%MULTIINVERSIONES_MIBANCO%'
          or tg_enlace like '%MULTIINVERSIONES_MIBANCO%' )
          or (  probsummarym1.company like '%BANCO%COOPERATIVO%DE%LOS%TRABAJADORES%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO%COOPERATIVO%DE%LOS%TRABAJADORES%'
          or probsummarym1.brief_description like '%BANCO%COOPERATIVO%DE%LOS%TRABAJADORES%'
          or probsummarym1.action like '%BANCO%COOPERATIVO%DE%LOS%TRABAJADORES%'
          or tg_enlace like '%BANCO%COOPERATIVO%DE%LOS%TRABAJADORES%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 96


-- COD 97
update p_service_m
   set
   id_interno = '97'
 where probsummarym1.company like '%PANACAFE%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%PANACAFE%'
          or probsummarym2.TG_COMPANY_CNOC like '%PANACAFE%'
          or probsummarym1.brief_description like '%PANACAFE%'
          or probsummarym1.action like '%PANACAFE%'
          or tg_enlace like '%PANACAFE%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 97


-- COD 98
update p_service_m
   set
   id_interno = '98'
 where probsummarym1.company like '%FEDECACES%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FEDECACES%'
          or probsummarym2.TG_COMPANY_CNOC like '%FEDECACES%'
          or probsummarym1.brief_description like '%FEDECACES%'
          or probsummarym1.action like '%FEDECACES%'
          or tg_enlace like '%FEDECACES%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 98


-- COD 99
update p_service_m
   set
   id_interno = '99'
 where CLIENTE like '%TALLER_DIDEA%'
    or CLIENTE like '%TALLERDIDEA%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%TALLER_DIDEA%'
          or probsummarym2.TG_COMPANY_CNOC like '%TALLER_DIDEA%'
          or probsummarym1.brief_description like '%TALLER_DIDEA%'
          or probsummarym1.action like '%TALLER_DIDEA%'
          or tg_enlace like '%TALLER_DIDEA%' )
          or (  probsummarym1.company like '%TALLERDIDEA%'
          or probsummarym2.TG_COMPANY_CNOC like '%TALLERDIDEA%'
          or probsummarym1.brief_description like '%TALLERDIDEA%'
          or probsummarym1.action like '%TALLERDIDEA%'
          or tg_enlace like '%TALLERDIDEA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 99

-- COD 100
update p_service_m
   set
   id_interno = '100'
 where CLIENTE like '%ALIMENTICIOS_DIANA%'
    or CLIENTE like '%ALIMENTICIOSDIANA%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%ALIMENTICIOS_DIANA%'
          or probsummarym2.TG_COMPANY_CNOC like '%ALIMENTICIOS_DIANA%'
          or probsummarym1.brief_description like '%ALIMENTICIOS_DIANA%'
          or probsummarym1.action like '%ALIMENTICIOS_DIANA%'
          or tg_enlace like '%ALIMENTICIOS_DIANA%' )
          or (  probsummarym1.company like '%ALIMENTICIOSDIANA%'
          or probsummarym2.TG_COMPANY_CNOC like '%ALIMENTICIOSDIANA%'
          or probsummarym1.brief_description like '%ALIMENTICIOSDIANA%'
          or probsummarym1.action like '%ALIMENTICIOSDIANA%'
          or tg_enlace like '%ALIMENTICIOSDIANA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 100


-- COD 101
update p_service_m
   set
   id_interno = '101'
 where probsummarym1.company like '%IMPRESSA%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%IMPRESSA%'
          or probsummarym2.TG_COMPANY_CNOC like '%IMPRESSA%'
          or probsummarym1.brief_description like '%IMPRESSA%'
          or probsummarym1.action like '%IMPRESSA%'
          or tg_enlace like '%IMPRESSA%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 101

-- COD 102
update p_service_m
   set
   id_interno = '102'
 where CLIENTE like '%FEDECREDITO%'
    or CLIENTE like '%FEDERACION_DE_CAJAS_DE_CREDITO%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%FEDECREDITO%'
          or probsummarym2.TG_COMPANY_CNOC like '%FEDECREDITO%'
          or probsummarym1.brief_description like '%FEDECREDITO%'
          or probsummarym1.action like '%FEDECREDITO%'
          or tg_enlace like '%FEDECREDITO%' )
          or (  probsummarym1.company like '%FEDERACION_DE_CAJAS_DE_CREDITO%'
          or probsummarym2.TG_COMPANY_CNOC like '%FEDERACION_DE_CAJAS_DE_CREDITO%'
          or probsummarym1.brief_description like '%FEDERACION_DE_CAJAS_DE_CREDITO%'
          or probsummarym1.action like '%FEDERACION_DE_CAJAS_DE_CREDITO%'
          or tg_enlace like '%FEDERACION_DE_CAJAS_DE_CREDITO%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 102

-- COD 103
update p_service_m
   set
   id_interno = '103'
 where CLIENTE like '%DISZASA%'
    or CLIENTE like '%DISTRIBUIDORA_SALVADORENA_SV%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%DISZASA%'
          or probsummarym2.TG_COMPANY_CNOC like '%DISZASA%'
          or probsummarym1.brief_description like '%DISZASA%'
          or probsummarym1.action like '%DISZASA%'
          or tg_enlace like '%DISZASA%' )
          or (  probsummarym1.company like '%DISTRIBUIDORA_SALVADORENA_SV%'
          or probsummarym2.TG_COMPANY_CNOC like '%DISTRIBUIDORA_SALVADORENA_SV%'
          or probsummarym1.brief_description like '%DISTRIBUIDORA_SALVADORENA_SV%'
          or probsummarym1.action like '%DISTRIBUIDORA_SALVADORENA_SV%'
          or tg_enlace like '%DISTRIBUIDORA_SALVADORENA_SV%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 103

-- COD 104
update p_service_m
   set
   id_interno = '104'
 where probsummarym1.company like '%DISTRIBUIDORA_DE_PINTURAS_Y_MATERIALES%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%DISTRIBUIDORA_DE_PINTURAS_Y_MATERIALES%'
          or probsummarym2.TG_COMPANY_CNOC like '%DISTRIBUIDORA_DE_PINTURAS_Y_MATERIALES%'
          or probsummarym1.brief_description like '%DISTRIBUIDORA_DE_PINTURAS_Y_MATERIALES%'
          or probsummarym1.action like '%DISTRIBUIDORA_DE_PINTURAS_Y_MATERIALES%'
          or tg_enlace like '%DISTRIBUIDORA_DE_PINTURAS_Y_MATERIALES%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 104


-- COD 106
update p_service_m
   set
   id_interno = '106'
 where probsummarym1.company like '%BANCO_ABANK%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BANCO_ABANK%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO_ABANK%'
          or probsummarym1.brief_description like '%BANCO_ABANK%'
          or probsummarym1.action like '%BANCO_ABANK%'
          or tg_enlace like '%BANCO_ABANK%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 106

-- COD 107
update p_service_m
   set
   id_interno = '107'
 where probsummarym1.company like '%BIMBO%'
   and tg_country_code = 'SV';

 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BIMBO%'
          or probsummarym2.TG_COMPANY_CNOC like '%BIMBO%'
          or probsummarym1.brief_description like '%BIMBO%'
          or probsummarym1.action like '%BIMBO%'
          or tg_enlace like '%BIMBO%' )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'EL SALVADOR'
   );   
{{* ********************************************************************* *}}
-- FIN 107

-- INICIO 109	

update p_service_m
   set
   id_interno = '109'
 where probsummarym1.company like '%BANCO%FICOHSA%'
   and tg_country_code = 'HN';


 
        from t_tickets_cerrados_cnoc_lite
       where ( (  probsummarym1.company like '%FICOHSAS%' )
          or (  probsummarym1.company like '%FICOHSA%'
          or probsummarym2.TG_COMPANY_CNOC like '%FICOHSA%'
          or probsummarym1.brief_description like '%FICOHSA%'
          or probsummarym1.action like '%FICOHSA%'
          -- tg_enlace_destino like '%FICOHSA%'
          or tg_enlace like '%CC\_FICOHSA\_HN%' escape '\' ) )
         and ( to_date(to_char(
            t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
            'DD/MM/YYYY'
         ),
           'DD/MM/YYYY') >= '01/02/2026'
         and to_date(to_char(
         t_tickets_cerrados_cnoc_lite."FECHA DE CIERRE",
         'DD/MM/YYYY'
      ),
        'DD/MM/YYYY') < '01/03/2026' )
         and pais = 'HONDURAS'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 109

-- COD 110
update p_service_m
   set
   id_interno = '110'
 where probsummarym1.company like '%BANCO%AGROMERCANTIL%'
   and ID_SM not like '%XT'
   and pais = 'GT';


 
        from t_tickets_cerrados_cnoc_lite
       where (  probsummarym1.company like '%BANCO AGROMERCANTIL%'
          or probsummarym2.TG_COMPANY_CNOC like '%BANCO AGROMERCANTIL%'
          or probsummarym1.brief_description like '%BANCO AGROMERCANTIL%'
          or probsummarym1.action like '%BANCO AGROMERCANTIL%'
          -- tg_enlace_destino like '%BANCO AGROMERCANTIL%'
          or tg_enlace like '%CC_BAM%' escape '\'
          or tg_enlace like '%BAM%' escape '\' )
         and "FECHA DE CIERRE" >= to_date('01/02/2026','DD/MM/YYYY')
         and "FECHA DE CIERRE" < to_date('01/03/2026','DD/MM/YYYY')
         and pais = 'GUATEMALA'
         and ID_SM not like '%XT'
   );
{{* ********************************************************************* *}}
-- FIN 110