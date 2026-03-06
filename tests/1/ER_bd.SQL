-- TABLAs 

empresas_catalogo
    COD
    pais
    STATUS 0 / 1
    ORDEN

-- PAG 7
parque_cnoc
    id_cliente
    mes
    ano 


lista
    id_cliente, 
    mes, 
    ano, 
    indicator_name, 
    indicator_value

-- PAG 6
hi_de_indicadores (id_cliente,
                        mes,
                        ano,
                        inci_menor_o_8,
                        inci_mayor_a_8,
                        productividad,
                        sitios_reincidentes,
                        indice_de_reincidencia,
                        mttr_promedio,
                        disponibilidad,
                        proactividad)  

/* ********************************************************************* */

-- "user": os.getenv("ORACLE_DB_USER", "SYS"),
        "password": os.getenv("ORACLE_DB_PASSWORD", "claro2022"),
        "dsn": os.getenv("ORACLE_DB_DSN", "172.17.222.210/xe"),
        "encoding": "UTF-8",

/* ********************************************************************* */
// =============================
// TABLA: empresas_catalogo
// =============================

Table empresas_catalogo {
  COD int [pk]
  pais varchar
  STATUS int  // 0 = inactivo, 1 = activo
  ORDEN int
}

// ==============================
// TABLA: parque_cnoc
// ==============================

Table parque_cnoc {
  id_cliente int
  mes int
  ano int

  indexes {
    (id_cliente, mes, ano)
  }
}

// ==============================
// TABLA: lista (indicadores dinámicos)
// ==============================

Table lista {
  id_cliente int
  mes int
  ano int
  indicator_name varchar
  indicator_value varchar

  indexes {
    (id_cliente, mes, ano)
  }
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
Ref: lista.id_cliente > empresas_catalogo.COD
Ref: hi_de_indicadores.id_cliente > empresas_catalogo.COD
