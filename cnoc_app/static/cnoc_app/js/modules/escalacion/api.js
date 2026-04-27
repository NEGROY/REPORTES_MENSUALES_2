import { ajax } from '../../helpers/ajax.js';

 /* ------------ * DEVUELVE LOS VALORES DE DATA DE LOS ENDPOINTS  * ------------ */
/* ANTES PRUEBAS MAS 
    export const getRow = (payload) => {
        if (!payload || !payload.ok) return [];  if (!Array.isArray(payload.data)) return [];
        return payload.data;     }; */

/* ------------ * DEVUELVE LOS VALORES DE DATA DE LOS ENDPOINTS  v2 * ------------ */ 
export function getData(payload) {
    if (!payload || payload.ok === false) return [];

    const data = payload.data;

    if (Array.isArray(data)) return data;
    if (typeof data === 'object' && data !== null) return [data];

    return [];
}

/* ------------ * Devuelve la primera fila de data * ------------ */
export function getFirstRow(payload) {
    const data = getData(payload);
    return data.length > 0 ? data[0] : {};
}

/* ------------ * ASIGNA VALORES A UN ARRAY DE INPUTS DEFINIDOS PREVIAMENTE * ------------ */
export function asignar_inputs_data(datos, inputs = []) {
   // console.log('🧩 MAPEO INPUTS:', inputs);
   console.log('📦 DATA:', datos);
    // validamos vacios
    if (!datos || typeof datos !== 'object') {
        console.warn('⚠️ data inválida');
        return;
    }
    
inputs.forEach(cfg => {
        const { id, field, default: def = "" } = cfg;
        const el = document.getElementById(id);

        if (!el) {
            console.warn(`⚠️ Elemento #${id} no existe`);
            return;
        }
        // Resolver valor SOLO por key
        let valor = datos[field];
        //  console.log(valor)
        if (valor === undefined || valor === null) {
            valor = def;
        }
        //console.log(`✅ ${id} ← datos["${field}"] =`, valor);
        // ✅ Asignar según tipo de elemento
        if (
            el.tagName === 'INPUT' ||
            el.tagName === 'TEXTAREA' ||
            el.tagName === 'SELECT'
        ) {
            el.value = valor;
        } else {
            el.textContent = valor;
        }
    });
}

/* ------------ * * ------------ */

export const escalacionApi = {
    async listarAreasPorPais(paisId) {
        const url = `/tablas/api/paises/${paisId}/areas/`;
        const response = await ajax.get(url);
        console.log('📦 listarAreasPorPais:', response);
        return response;
    },

   async obtenerMasivaDetalle(tk) {
        const url = `/api/masivas/${encodeURIComponent(tk)}/`;
        const response = await ajax.get(url);
        console.log('📦 obtenerMasivaDetalle:', response);
        return response;
    },

    async generarTablaEscalacion(payload) {
        const url = '/tablas/api/calculadora/';
        const response = await ajax.post(url, payload);
        console.log('📦 generarTablaEscalacion:', response);
        return response;
    }
};

/* ------------ * * ------------ */

/* ------------ * * ------------ */

/* ------------ * * ------------ */
/* -------------------------- */
