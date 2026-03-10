 
/* ********************************************************************* */
        -- "user": os.getenv("ORACLE_DB_USER", "SYS"),
        "password": os.getenv("ORACLE_DB_PASSWORD", "claro2022"),
        "dsn": os.getenv("ORACLE_DB_DSN", "172.17.222.210/xe"),
        "encoding": "UTF-8",
/* ************************** ============================= ******************************************* */



// =============================
// TABLA: empresas_catalogo
// =============================
Table empresas_catalogo {
  COD int [pk]
  pais varchar
  STATUS int  // 0 = inactivo, 1 = activo
  ORDEN int
  id_indice int //TIPO DE REPORTE MENSUAL ()
}

// ==============================
// TABLA: parque_cnoc // pag 7, ComportamientoREDdeCLIENTE
// ==============================
Table parque_cnoc { 
  id_cliente int
  mes int
  ano int
  sitios_activos int
  tt_EnlacesDatos int //Total de Enlaces de datos 
  internet int  
  AE int
  tt_tt int  // Total de TT 
  //indexes { (id_cliente, mes, ano) }
}

// ==============================
// TIPOS DE REPORTE // PAGINAS DE REPORTES 
Table pag_reporte{
  id  int
  titulo varchar
  categoria varchar
  estado bool
}

// ==============================
// TIPOS DE REPORTE // PAGINAS DE REPORTES 
Table INDICE_REPORTE{
  id  int
  tipos varchar
  p1 int
  p2 int
  p3 int
  p4 int
  p5 int
  p6 int
  p7 int
  p8 int
  p9 int
  p10 int
  p11 int
  p12 int
  p13 int
  p14 int
  p16 int
  p17 int
  p18 int
  p19 int
  p20 int
  p21 int
}

// ==============================
// TABLA: hi_de_indicadores
// ==============================
Table hi_de_indicadores {
  id_cliente int
  mes int
  ano int
  inci_menor_o_8 number
  inci_mayor_a_8 number
  productividad number
  sitios_reincidentes number
  indice_de_reincidencia number
  mttr_promedio number
  disponibilidad number
  proactividad number

  indexes {
    (id_cliente, mes, ano)
  }
}

// ==============================
// RELACIONES
// ==============================

Ref: parque_cnoc.id_cliente > empresas_catalogo.COD
Ref: hi_de_indicadores.id_cliente > empresas_catalogo.COD

Ref: "empresas_catalogo"."id_indice" < "INDICE_REPORTE"."id"

















/* ************************** ============================= ******************************************* */