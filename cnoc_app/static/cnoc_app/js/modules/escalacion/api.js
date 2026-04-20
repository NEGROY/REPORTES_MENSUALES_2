import { ajax } from '../../helpers/ajax.js';

export const escalacionApi = {
    async listarAreasPorPais(paisId) {
        const url = `/tablas/api/paises/${paisId}/areas/`;
        console.log('🌐 URL consultada:', url);
        const response = await ajax.get(url);
        console.log('📦 Response cruda listarAreasPorPais:', response);

        return response;
    },
};

 