// import {getData, asignar_inputs_data } from './api.js';
import { escalacionApi, getData, getFirstRow, asignar_inputs_data } from './api.js';
// # LAS APIS 
// import {escalacionApi} from '../cnoc/api.js';

/* ESTRUCTURA PARA LOS INPUTS */
    /* inputs para tablas de escalacion  /api/masivas/F6843026/ */
 const MAPEO_INPUTS_ESCALACION = [
    { id: "titulo", field: "TITULO" },
    { id: "falla_dire", field: "TG_ENLACE_DESTINO"},
    { id: "open_time", field: "OPEN_TIME" },
    { id: "cierre", field: "CLOSE_TIME" },
    { id: "compannia", field: "COMPANY" },
  ]
/* const MAPEO_INPUTS_ESCALACION = [
    { id: "falla", field: "TK" },
    { id: "titulo", field: "TITULO" },
    { id: "company", field: "COMPANY" },
    { id: "falla_dire", field: "TG_ENLACE_DESTINO" },
    { id: "open_time", field: "OPEN_TIME" },
    { id: "cierre", field: "CLOSE_TIME" },
    { id: "tiempoAcumulado", field: "HH_MM_SS" },
    { id: "totalHoras", field: "TOTAL_MENOS_CLIENTE_HORAS" },
]; */
 
const ICONS = {
    comment: '/static/icon/comment.svg',
    plus: '/static/icon/plus.svg',
    right: '/static/icon/right.svg',
};

/* ESTRUCTURA PARA LOS INPUTS */

 /* console.log('✅ tablas_escalacion.html cargado'); */
 /* ************************ ------------------ ************************ */
document.addEventListener('DOMContentLoaded', () => {
    const selectPais = document.getElementById('pais');
    const selectAreas = document.getElementById('areasxpais');
    const inputFalla = document.getElementById('falla');
    const btnBuscar = document.getElementById('btnBuscar');

    /* validamos que si existan  */
    if (!btnBuscar) return;
    if (!selectPais || !selectAreas) { return; }
    // DESAVILITAMOS EL BUTON DE BUSCAR API 
    btnBuscar.disabled = true;
    // console.log("holas");
    selectPais.addEventListener('change', async function () {
        const paisId = this.value;
        /* limpieza y validacion de formulario */
        resetAreas();
        validarFormulario();
        /* ---------- */
        if (!paisId || paisId === '0') {
            return;
        }
        /* ---------- */
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

    /* EN CADA CAMBIO DEL FORMULARIO VAMOS A validar los campos   */
    selectAreas.addEventListener('change', validarFormulario);
    inputFalla.addEventListener('input', validarFormulario);
/* **************************************************************************************************************************** */


/* **************************************************************************************************************************** */
/* ------------- BLOQUES DE CODIGO PARA LA 
    VALIDACION DEL FORMALARIO, PAIS, AREA Y FALLA  */
    function validarFormulario() {
        console.clear();
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
/* -  SENCILLO, DESPUES CAMBIAR AL HELPER DE DOM   - */ 
    function renderAreas(areas) {
        resetAreas('---Seleccione un área---');

        areas.forEach((area) => {
            const option = document.createElement('option');
            option.value = area.id;
            option.textContent = area.nombre_area;
            selectAreas.appendChild(option);
        });
    }

    /*     AL PRECIONAR EL BOTON   */
    btnBuscar.addEventListener("click", buscarDatos_api); 

    /*  FUNCION DE PRUEBA PARA EJECUTAR LA CONSULTA DE MI ENBDPOINT que esta aqui  */
    async function buscarDatos_api() {
      console.clear(); // console.log("🟢 Click en Buscar");
        /* if (typeof toggleLoader === "function") toggleLoader(1);     */
        /* en vez de obtener el dato lo mejor es que se lo enviemos */
          const tk = (document.getElementById("falla")?.value || "").trim();
          if (!tk) {
            console.warn("⚠️ No se ingresó falla");
            toggleLoader?.(0);
            return;
          }
          /* aqui colocamos la api endpoint */
          const url = `/api/masivas/${encodeURIComponent(tk)}/`;
          console.log("🌐 URL:", url);
          try {
            const resp = await fetch(url, {
              method: "GET",
              headers: { "Accept": "application/json" }
            });
        
            const payload = await resp.json();
            //console.log("📦 RESPUESTA COMPLETA:", payload);
            if (!resp.ok || payload?.ok === false) {
              console.error("❌ Error backend:", payload);
              return;
            }
            // aquí ves SOLO el registro principal
            const rows = getData(payload);
            // console.log("✅ ROW NORMALIZADA:", rows);
            // PARA  llenar inputs
            asignar_inputs_data(rows[0], MAPEO_INPUTS_ESCALACION);
          } catch (err) {
            console.error("🔥 Error JS:", err);
          } finally {
           /* toggleLoader?.(0); */
           console.log("toggleLoader");
          }
    }

/* **************************************************************************************************************************** */
function getTipoIcon(tipo = '') {
    const value = String(tipo || '').toLowerCase();

    if (value.includes('tel')) return '📞';
    if (value.includes('mail')) return '✉️';
    if (value.includes('teams')) return '🟣';
    if (value.includes('whatsapp')) return '🟢';

    return '•';
}


/* **************************************************************************************************************************** */
function renderTablaEscalacion(rows = []) {
    const div = document.getElementById('TB_calcu');
    if (!div) return;

    if (!Array.isArray(rows) || rows.length === 0) {
        div.innerHTML = `
            <div class="text-center py-5 text-muted">
                <p class="mb-0">No hay datos para mostrar en la tabla de escalación.</p>
            </div> `;
        return;
    }
    window.__tablaEscalacionRows = rows;

    let html = `
        <div class="table-responsive">
            <table class="table table-striped table-hover table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Nombre</th>
                        <th>Medio</th>
                        <th>Tiempo</th>
                        <th>Calculadora</th>
                        <th>Opciones</th>
                    </tr>
                </thead>
                <tbody>    `;

    rows.forEach((item, index) => {
        const comentarioBadge = item.comentario
            ? `<span class="badge bg-light text-dark">${item.comentario}</span>`
            : '';

        html += `
            <tr>
                <td>${item.nivel}</td>
                <td>${item.nombre} ${comentarioBadge}</td>
                <td>${item.telefono} ${getTipoIcon(item.tipo)}</td>
                <td>${item.tiempo} Horas</td>
                <td><label class="form-label">${item.hr_suma} Hrs</label></td>
                <td>
                    <button type="button"
                        class="btn btn-outline-secondary btn-sm rounded-pill shadow-sm px-3"
                        onclick="window.mnsjEscala && mnsjEscala(window.__tablaEscalacionRows[${index}].action_data)"
                        title="Genera mensajes">
                        <img src="${ICONS.comment}" alt="comment" style="width:1.4em; height:1.4em; vertical-align:middle;">
                    </button>

                    <button type="button"
                        class="btn btn-outline-secondary btn-sm rounded-pill shadow-sm px-3"
                        onclick="window.toggleTable && toggleTable(window.__tablaEscalacionRows[${index}].action_data)"
                        title="+2 horas">
                        <img src="${ICONS.plus}" alt="plus" style="width:1.4em; height:1.4em; vertical-align:middle;">
                    </button>

                    <button type="button"
                        class="btn btn-outline-success btn-sm rounded-pill shadow-sm px-3"
                        onclick="window.tablerosave && tablerosave(window.__tablaEscalacionRows[${index}].action_data)"
                        title="Escalación">
                        <img src="${ICONS.right}" alt="right" style="width:1.4em; height:1.4em; vertical-align:middle;">
                    </button>
                </td>
            </tr> `;
    });

    html += ` </tbody>
            </table>
        </div>
        <div id="tableContainer"></div>    `;

    div.innerHTML = html;
}

async function buscarDatos_api() {
    console.clear();

    const tk = (document.getElementById("falla")?.value || "").trim();
    const areaId = document.getElementById('areasxpais')?.value || '';
    const nivel = document.getElementById('acumulado')?.value || '1';

    if (!tk) {
        console.warn("⚠️ No se ingresó falla");
        toggleLoader?.(0);
        return;
    }

    if (!areaId) {
        console.warn("⚠️ No se seleccionó área");
        return;
    }

    const url = `/api/masivas/${encodeURIComponent(tk)}/`;
    console.log("🌐 URL:", url);

    try {
        const resp = await fetch(url, {
            method: "GET",
            headers: { "Accept": "application/json" }
        });

        const payload = await resp.json();

        if (!resp.ok || payload?.ok === false) {
            console.error("❌ Error backend:", payload);
            return;
        }

        const rows = getData(payload);
        const row = rows[0] || {};

        console.log('✅ row masiva:', row);

        asignar_inputs_data(row, MAPEO_INPUTS_ESCALACION);

        const calculadoraPayload = {
            area_id: areaId,
            nivel: nivel,
            falla_data: row,
        };

        const tablaPayload = await escalacionApi.generarTablaEscalacion(calculadoraPayload);

        if (!tablaPayload?.ok) {
            console.error('❌ Error calculadora:', tablaPayload);
            return;
        }

        renderTablaEscalacion(tablaPayload.data?.rows || []);
    } catch (err) {
        console.error('🔥 Error JS:', err);
    }
}

window.buscarDatos_api = buscarDatos_api;




/* **************************************************************************************************************************** */



/* **************************************************************************************************************************** */

});

/* 
// BOTON PARA BUSCAR  LA FALLA ()
//  const url = `http://172.20.97.102:8503/masivas/${tkEntrada}?token=masivas2025`;
function buscarDatos_api(){
    console.log("PRUEBAS ESTAS");
}
*/ 
// FUNCION PARA LIMPIAR AREAS DE TXT MENSAJES Y TAMBIEN ALGUNOS DIVS, inputs

// ToggleLoader LOADER DEBEMOS DE AGREGAR UN LOADER

// FUNCION PARA IMPRIMIMOS EL PROCEDSO DE AL MOMENTO DE GENERRAR LA TABLAS 

