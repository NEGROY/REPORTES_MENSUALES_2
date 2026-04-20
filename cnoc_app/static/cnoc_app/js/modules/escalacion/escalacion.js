import { escalacionApi } from './api.js';

 console.log('✅ tablas_escalacion.html cargado');

document.addEventListener('DOMContentLoaded', () => {
    const selectPais = document.getElementById('pais');
    const selectAreas = document.getElementById('areasxpais');

    if (!selectPais || !selectAreas) {
        return;
    }
    console.log("holas");

    const resetAreas = (message = '---Seleccione un país---') => {
        selectAreas.innerHTML = `<option value="">${message}</option>`;
    };

    const renderAreas = (areas) => {
        resetAreas('---Seleccione un área---');

        areas.forEach((area) => {
            const option = document.createElement('option');
            option.value = area.id;
            option.textContent = area.nombre_area;
            selectAreas.appendChild(option);
        });
    };

    selectPais.addEventListener('change', async function () {
        const paisId = this.value;

        if (!paisId || paisId === '0') {
            resetAreas();
            return;
        }

        try {
            const response = await escalacionApi.listarAreasPorPais(paisId);

            if (!response.ok) {
                resetAreas('---Sin áreas disponibles---');
                return;
            }

            renderAreas(response.data || []);
        } catch (error) {
            console.error('Error cargando áreas:', error);
            resetAreas('---Error al cargar áreas---');
        }
    });
});