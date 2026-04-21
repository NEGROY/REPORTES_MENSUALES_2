import { escalacionApi } from './api.js';

 /* console.log('✅ tablas_escalacion.html cargado'); */

 /* ************************ ------------------ ************************ */
document.addEventListener('DOMContentLoaded', () => {
    const selectPais = document.getElementById('pais');
    const selectAreas = document.getElementById('areasxpais');
    const inputFalla = document.getElementById('falla');
    const btnBuscar = document.getElementById('btnBuscar');

    // DESAVILITAMOS EL BUTON DE BUSCAR API 
    btnBuscar.disabled = true;

    if (!selectPais || !selectAreas) {
        return;
    }

    // console.log("holas");
    selectPais.addEventListener('change', async function () {
        const paisId = this.value;

        resetAreas();
        validarFormulario();

        if (!paisId || paisId === '0') {
            return;
        }

        try {
            const response = await escalacionApi.listarAreasPorPais(paisId);
            if (!response.ok) {
                resetAreas('---Sin áreas disponibles---');
                validarFormulario();
                return;
            }
            renderAreas(response.data || []);
            validarFormulario();
        } catch (error) {
            console.error('❌ Error cargando áreas:', error);
            resetAreas('---Error al cargar áreas---');
            validarFormulario();
        }
    });

    selectAreas.addEventListener('change', validarFormulario);
    inputFalla.addEventListener('input', validarFormulario);
/* ************************************************************** */

/* ------------- BLOQUES DE CODIGO PARA LA 
    VALIDACION DEL FORMALARIO, PAIS, AREA Y FALLA  */
    function validarFormulario() {
        const paisValido = selectPais.value && selectPais.value !== '0';
        const areaValida = selectAreas.value && selectAreas.value !== '';
        const fallaValida = inputFalla.value.trim() !== '';

        btnBuscar.disabled = !(paisValido && areaValida && fallaValida);

        console.log(' validarFormulario', {
            pais: selectPais.value,
            area: selectAreas.value,
            falla: inputFalla.value.trim(),
            habilitado: !btnBuscar.disabled,
        });
    }
/* - VALIDA QUE RESETEA EL AREA CADA VEZ  - */ 
    function resetAreas(mensaje = '---Seleccione un país---') {
        selectAreas.innerHTML = `<option value="">${mensaje}</option>`;
        selectAreas.value = '';
    }
/* -    - */ 
    function renderAreas(areas) {
        resetAreas('---Seleccione un área---');

        areas.forEach((area) => {
            const option = document.createElement('option');
            option.value = area.id;
            option.textContent = area.nombre_area;
            selectAreas.appendChild(option);
        });
    }


});

// BOTON PARA BUSCAR  LA FALLA ()
//  const url = `http://172.20.97.102:8503/masivas/${tkEntrada}?token=masivas2025`;
function buscarDatos_api(){
    console.log("PRUEBAS ESTAS");
}

// FUNCION PARA LIMPIAR AREAS DE TXT MENSAJES Y TAMBIEN ALGUNOS DIVS, inputs

// ToggleLoader LOADER DEBEMOS DE AGREGAR UN LOADER

// FUNCION PARA IMPRIMIMOS EL PROCEDSO DE AL MOMENTO DE GENERRAR LA TABLAS 

