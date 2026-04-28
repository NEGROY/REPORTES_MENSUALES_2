// import {getData, asignar_inputs_data } from './api.js';
import { escalacionApi, getData, asignar_inputs_data } from './api.js';
import { tb_copy, mnsjEscala } from './messages.js';
import { formatDateValue, normalizeDateForBackend, getCurrentDateTimeLocal  } from '../../helpers/dates.js';
import { abrirModalRelojes, registrarEventosClocks } from './clocks.js';

// # LAS APIS
// import {escalacionApi} from '../cnoc/api.js';

/* ESTRUCTURA PARA LOS INPUTS */
/* inputs para tablas de escalacion /api/masivas/F6843026/ */
const MAPEO_INPUTS_ESCALACION = [
    { id: "titulo", field: "TITULO" },
    { id: "falla_dire", field: "TG_ENLACE_DESTINO" },
    { id: "compannia", field: "COMPANY" },
    // Fechas
    { id: "open_time", field: "OPEN_TIME", isDate: true, dateMode: "sql" },
    { id: "cierre", field: "CLOSE_TIME", isDate: true, dateMode: "sql" },
];

// # ICONOS RUTAS
const ICONS = {
    comment: '/static/icon/comment.svg',
    plus: '/static/icon/plus.svg',
    right: '/static/icon/right.svg',
};

/* ============================
   ESTADO DEL MÓDULO
============================ */
const escalacionState = {
    fallaActual: null,
};

/* console.log('✅ tablas_escalacion.html cargado'); */

document.addEventListener('DOMContentLoaded', () => {
    const selectPais = document.getElementById('pais');
    const selectAreas = document.getElementById('areasxpais');
    const inputFalla = document.getElementById('falla');
    const btnBuscar = document.getElementById('btnBuscar');
    const btnCalcularTabla = document.getElementById('btnCalcularTabla');
    const btnRelojes = document.getElementById('btnRelojes');

    /* validamos que si existan */
    if (!btnBuscar) return;
    if (!selectPais || !selectAreas || !inputFalla) return;

    // VALIDA RELOJES 
    if (btnRelojes) {
            btnRelojes.addEventListener('click', async () => {
                const tk = validarTicket(document.getElementById('falla')?.value || '');
                if (!tk) return;
                await abrirModalRelojes(tk);
            });
        }
        registrarEventosClocks();


    // DESHABILITAMOS EL BOTON DE BUSCAR API
    btnBuscar.disabled = true;

    selectPais.addEventListener('change', async function () {
        const paisId = this.value;

        /* limpieza y validacion de formulario */
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

    /* EN CADA CAMBIO DEL FORMULARIO VAMOS A validar los campos */
    selectAreas.addEventListener('change', validarFormulario);
    inputFalla.addEventListener('input', validarFormulario);

    /* BOTON PARA BUSCAR LA FALLA */
    btnBuscar.addEventListener('click', buscarDatos_api);

    /* Registra el botón Calcular */
    if (btnCalcularTabla) {
        btnCalcularTabla.addEventListener('click', async () => {
            await recalcularTablaEscalacion();
        });
    }

    /* Relojes (placeholder por ahora) */
   if (btnRelojes) {
        btnRelojes.addEventListener('click', async () => {
            const tk = validarTicket(document.getElementById('falla')?.value || '');
            if (!tk) return;

            await abrirModalRelojes(tk);
        });
    }

    /* ------------- BLOQUES DE CODIGO PARA LA
       VALIDACION DEL FORMULARIO, PAIS, AREA Y FALLA */
    function validarFormulario() {
        const paisValido = !!selectPais.value && selectPais.value !== '0';
        const areaValida = !!selectAreas.value && selectAreas.value !== '';
        const fallaValida = !!inputFalla.value.trim();

        btnBuscar.disabled = !(paisValido && areaValida && fallaValida);

        console.log('🔎 validarFormulario', {
            pais: selectPais.value,
            area: selectAreas.value,
            falla: inputFalla.value.trim(),
            habilitado: !btnBuscar.disabled,
        });
    }

    /* - VALIDA QUE RESETEA EL AREA CADA VEZ - */
    function resetAreas(mensaje = '---Seleccione un país---') {
        selectAreas.innerHTML = `<option value="">${mensaje}</option>`;
        selectAreas.value = '';
    }

    /* - SENCILLO, DESPUES CAMBIAR AL HELPER DE DOM - */
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

/* **************************************************************************************************************************** */
/* VALIDACIONES GENERALES */
function validarTicket(tk = '') {
    const value = String(tk || '').trim().toUpperCase();

    if (!value) {
        console.warn('⚠️ No hay falla cargada');
        return null;
    }

    return value.startsWith('F') ? value : `F${value}`;
}

function validarArea(areaId = '') {
    const value = String(areaId || '').trim();

    if (!value || value === '0') {
        console.warn('⚠️ No se seleccionó área');
        return null;
    }

    return value;
}

function validarNivel(nivel = '1') {
    const value = String(nivel || '').trim();
    const parsed = Number(value);

    if (!Number.isFinite(parsed) || parsed <= 0) {
        return '1';
    }

    return String(Math.trunc(parsed));
}

function validarHoraActual(raw = '') {
    const value = normalizeDateForBackend(raw);

    if (!value) {
        console.warn('⚠️ No hay HORA válida para recalcular');
        return null;
    }

    return value;
}

/* **************************************************************************************************************************** */
/* OBTENER FALLA ACTUAL */
async function obtenerFallaActualParaCalculo(tk) {
    // reutiliza si ya está cargada y coincide
    if (
        escalacionState.fallaActual &&
        String(escalacionState.fallaActual.TK || '').trim().toUpperCase() === tk
    ) {
        return escalacionState.fallaActual;
    }

    // fallback: volver a consultar detalle
    const payload = await escalacionApi.obtenerMasivaDetalle(tk);
    const rows = getData(payload);
    const row = rows[0] || null;

    if (!row) {
        console.warn('⚠️ No se encontró información de la falla');
        return null;
    }

    escalacionState.fallaActual = row;
    return row;
}

/* **************************************************************************************************************************** */
function getTipoIcon(tipo = '') {
    const value = String(tipo || '').trim().toLowerCase();
    const basePath = '/static/icon/';
    let icon = '';

    switch (value) {
        case 'llamada':
            icon = 'phone.svg';
            break;

        case 'whatsapp':
            icon = 'whatsapp.svg';
            break;

        case 'correo':
            icon = 'envelope.svg';
            break;

        case 'teams':
            icon = 'teams.svg';
            break;

        case 'llamada & teams':
            icon = 'llamadaTeams.svg';
            break;

        default:
            return '';
    }

    return `
        <span style="vertical-align:middle;">
            <img
                src="${basePath}${icon}"
                alt="${value}"
                width="16"
                height="16"
                class="icon"
                style="vertical-align:middle;"
            >
        </span>
    `;
}

/* **************************************************************************************************************************** */
function renderTablaEscalacion(rows = [], meta = {}) {
    const div = document.getElementById('TB_calcu');
    if (!div) return;

    if (!Array.isArray(rows) || rows.length === 0) {
        div.innerHTML = `
            <div class="text-center py-5 text-muted">
                <p class="mb-0">No hay datos para mostrar en la tabla de escalación.</p>
            </div>
        `;
        return;
    }

    window.__tablaEscalacionRows = rows;

    let html = `
        <div class="table-responsive">
            <table class="table table-sm table-hover table-bordered mb-0">
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
                <tbody>
    `;

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
            </tr>
        `;
    });

    html += `
                </tbody>
            </table>
        </div>
        <div id="tableContainer"></div>
    `;

    div.innerHTML = html;

    // AL CARGAR LA TABLA TAMBIÉN GENERAMOS EL TEXTO PARA COPIAR
    if (meta?.titulo && meta?.falla_id && meta?.hr_actual && meta?.area_id) {
        tb_copy(
            meta.titulo,
            meta.falla_id,
            meta.hr_actual,
            meta.tmp_acumu || '',
            meta.area_id
        );
    }
}

/* **************************************************************************************************************************** */
/* BOTON PARA BUSCAR LA FALLA */
/* // const url = `http://172.20.97.102:8503/masivas/${tkEntrada}?token=masivas2025`; */
async function buscarDatos_api() {
    console.clear();

    const tk = validarTicket(document.getElementById('falla')?.value || '');
    const areaId = validarArea(document.getElementById('areasxpais')?.value || '');
    const nivel = validarNivel(document.getElementById('acumulado')?.value || '1');

    if (!tk || !areaId) {
        return;
    }

    const url = `/api/masivas/${encodeURIComponent(tk)}/`;
    console.log('🌐 URL:', url);

    try {
        const resp = await fetch(url, {
            method: 'GET',
            headers: { Accept: 'application/json' }
        });

        const payload = await resp.json();

        if (!resp.ok || payload?.ok === false) {
            console.error('❌ Error backend:', payload);
            return;
        }

        const rows = getData(payload);
        const row = rows[0] || {};

        console.log('✅ row masiva:', row);

        // guardar la falla actual para recalcular después
        escalacionState.fallaActual = row;

        asignar_inputs_data(row, MAPEO_INPUTS_ESCALACION);

        // current_time inicia con OPEN_TIME
        const currentTimeInput = document.getElementById('current_time');
        if (currentTimeInput) {
            currentTimeInput.value = getCurrentDateTimeLocal();
        }

        // habilitar botones
        const btnCalcularTabla = document.getElementById('btnCalcularTabla');
        const btnRelojes = document.getElementById('btnRelojes');

        if (btnCalcularTabla) btnCalcularTabla.disabled = false;
        if (btnRelojes) btnRelojes.disabled = false;

        // PRIMER CÁLCULO AUTOMÁTICO AL CARGAR LA FALLA
        const calculadoraPayload = {
            area_id: areaId,
            nivel: nivel,
            falla_data: row,
        };

        const tablaPayload = await escalacionApi.generarTablaEscalacion(calculadoraPayload);

        console.log('📦 tablaPayload:', tablaPayload);

        if (!tablaPayload || tablaPayload.ok !== true) {
            console.error(
                '❌ Error calculadora:',
                tablaPayload?.message || tablaPayload?.error || tablaPayload
            );
            return;
        }

        renderTablaEscalacion(
            tablaPayload.data?.rows || [],
            tablaPayload.data?.meta || {}
        );

    } catch (err) {
        console.error('🔥 Error JS:', err);
    }
}

/* **************************************************************************************************************************** */
async function recalcularTablaEscalacion() {
    const tk = validarTicket(document.getElementById('falla')?.value || '');
    const areaId = validarArea(document.getElementById('areasxpais')?.value || '');
    const nivel = validarNivel(document.getElementById('acumulado')?.value || '1');
    const hrActualOverride = validarHoraActual(document.getElementById('current_time')?.value || '');

    if (!tk || !areaId || !hrActualOverride) {
        return;
    }

    try {
        const fallaData = await obtenerFallaActualParaCalculo(tk);

        if (!fallaData || typeof fallaData !== 'object') {
            console.warn('⚠️ fallaData inválida para cálculo');
            return;
        }

        const calculadoraPayload = {
            area_id: areaId,
            nivel: nivel,
            falla_data: fallaData,
            hr_actual_override: hrActualOverride,
        };

        console.log('📦 recalcular payload:', calculadoraPayload);

        const tablaPayload = await escalacionApi.generarTablaEscalacion(calculadoraPayload);

        console.log('📦 tablaPayload:', tablaPayload);

        if (!tablaPayload || tablaPayload.ok !== true) {
            console.error(
                '❌ Error calculadora:',
                tablaPayload?.message || tablaPayload?.error || tablaPayload
            );
            return;
        }

        renderTablaEscalacion(
            tablaPayload.data?.rows || [],
            tablaPayload.data?.meta || {}
        );

    } catch (error) {
        console.error('🔥 Error recalcularTablaEscalacion:', error?.data || error);
    }
}

/* **************************************************************************************************************************** */
/* EXPONER FUNCIONES GLOBALES PARA BOTONES INLINE */
window.buscarDatos_api = buscarDatos_api;
window.mnsjEscala = mnsjEscala;
window.tb_copy = tb_copy;

/*
 // BOTON PARA BUSCAR LA FALLA ()
 // const url = `http://172.20.97.102:8503/masivas/${tkEntrada}?token=masivas2025`;
 function buscarDatos_api(){
     console.log("PRUEBAS ESTAS");
 }
*/

// FUNCION PARA LIMPIAR AREAS DE TXT MENSAJES Y TAMBIEN ALGUNOS DIVS, inputs
// ToggleLoader LOADER DEBEMOS DE AGREGAR UN LOADER
// FUNCION PARA IMPRIMIMOS EL PROCEDSO DE AL MOMENTO DE GENERRAR LA TABLAS