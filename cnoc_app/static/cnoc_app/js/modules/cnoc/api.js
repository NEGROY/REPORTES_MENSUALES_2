import { ajax } from '../../helpers/ajax.js';

/* ******************************** */
export const cnocApi = {
    historialDiario(payload) {
        return ajax.post('/api/cnoc/historial-diario/', payload);
    },
};

/* ************ http://127.0.0.1:8000/api/cnoc/busqueda-tk/F6433510/ ****************** */
export const cnocApi = {
    buscarTk(fallaId) {
        return ajax.get(`/api/cnoc/busqueda-tk/${encodeURIComponent(fallaId)}/`);
    },
};




/* 
7) Ejemplo de consumo con fetch
Archivo: C:\laragon\www\REPORTES_MENSUALES_2\cnoc_app\static\cnoc_app\js\modules\cnoc\api.js

recuerda que asi lo consumiamos en php 
    $fecha_inicio_api = date('Ymd', strtotime($fecha_inicio));
    $fecha_fin_api    = date('Ymd', strtotime($fecha_fin));
    // URL del API
    $url = "http://172.20.97.102:8080/HistorialDiario";
    // Datos a enviar
    $data = [
        "operador" => $operador,
        "fecha_inicio" => $fecha_inicio_api,
        "fecha_fin" => $fecha_fin_api
    ];

    Ejemplo de request JSON
    {
      "operador": "NERY DIAZ",
      "fecha_inicio": "2026-04-01",
      "fecha_fin": "2026-04-21"
    }

*/