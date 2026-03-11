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
  razon_social varchar
  tt_sitioa int
  pais varchar
  STATUS int  // 0 = inactivo, 1 = activo
  ORDEN int // COMO SE ENVIA EL CORREO
  donde text // WHERE DE LA CONSULTA
  tipo varchar // CONEXION CON EL INDICE_REPORTE
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
// REPORTE ESTA TABLA CONTIENE EL ORDEN DE LAS TABLAS
Table pag_reporte{
  id  int
  id_cliente int
  cliente varchar
  paginas text // JSON [1,...23]
  estado bool
}

// ==============================
// listado de las paginas de los reportes 
Table INDICE_REPORTE{
  id  int
  titulo varchar
  MENSUALES BOOL 
  XT BOOL  // 
  banrural bool
  CNAM bool
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
 



  

/* ************************** ============================= ******************************************* */