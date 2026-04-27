import { ajax } from '../../helpers/ajax.js';

/* ESTA ES PARA REALIZAR PRUEBAS para consumir las diferentes APIS  */
export const escalacionApi = {
    async listarAreasPorPais(paisId) {
        console.clear();
        const url = `/tablas/api/paises/${paisId}/areas/`;
        /*  console.log('🌐 URL consultada:', url); */ 
        /* EJECUTA LA CONSULTA HACIA LA API  */ 
        const response = await ajax.get(url);
        // console.log('📦 Response cruda listarAreasPorPais:', response);
        return response;
    },

    //  ** endpoint obtenerMasivaDetalle
    async obtenerMasivaDetalle(tk) {
        const url = `/api/masivas/${encodeURIComponent(tk)}/`;
        const response = await ajax.get(url);
        console.log('📦 obtenerMasivaDetalle:', response);
        return response;
    }, 
    // ** another bite the dust

    // ** AQUI VAMOS AGREGANDO TOOODAS LOS ENDPOINTS QUE VAMOS REAQLIZANDO 
};
