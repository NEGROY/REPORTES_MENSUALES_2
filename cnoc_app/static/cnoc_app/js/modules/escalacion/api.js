import { ajax } from '../../helpers/ajax.js';
import { formatDateValue } from '../../helpers/dates.js';

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
        const {
            id,
            field,
            default: def = "",
            isDate = false,
            dateMode = 'display',
        } = cfg;

        const el = document.getElementById(id);
        if (!el) return;

        let value = def;

        if (typeof field === 'function') {
            value = field(datos);
        } else if (Array.isArray(field)) {
            for (const f of field) {
                const candidate = datos[f];
                if (candidate !== undefined && candidate !== null && String(candidate).trim() !== '') {
                    value = candidate;
                    break;
                }
            }
        } else {
            value = datos[field] ?? def;
        }

        if (isDate) {
            value = formatDateValue(value, dateMode);
        }

        if (["INPUT", "TEXTAREA", "SELECT"].includes(el.tagName)) {
            el.value = value ?? def;
        } else {
            el.textContent = value ?? def;
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
        console.log('📦 generarTablaEscalacion:' ); //, response
        return response;
    },

    async generarMensajeTabla(payload) {
        const url = '/tablas/api/mensaje-tabla/';
        return await ajax.post(url, payload);
        console.log('📦 generarMensajeTabla:', response);
    }


};

/* ------------ * * ------------ */



/* ------------ * * ------------ */

/* ------------ * * ------------ */
/* -------------------------- */
