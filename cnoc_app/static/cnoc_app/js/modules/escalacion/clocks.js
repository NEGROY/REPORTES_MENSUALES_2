import { escalacionApi, getData } from './api.js';

const clocksState = {
    rows: [],
};

function parseTiempoToSeconds(tiempo = '') {
    const value = String(tiempo || '').trim();
    if (!value) return 0;

    const parts = value.split(' ');
    let dias = 0;
    let timePart = '';

    if (parts.length === 2) {
        dias = parseInt(parts[0], 10) || 0;
        timePart = parts[1];
    } else {
        timePart = parts[0];
    }

    const [hh = '0', mm = '0', ss = '0'] = timePart.split(':');

    return (
        (dias * 86400) +
        (parseInt(hh, 10) * 3600) +
        (parseInt(mm, 10) * 60) +
        parseInt(ss, 10)
    );
}

function formatSecondsToTiempo(totalSegundos = 0) {
    const dias = Math.floor(totalSegundos / 86400);
    let resto = totalSegundos % 86400;

    const horas = Math.floor(resto / 3600);
    resto = resto % 3600;

    const minutos = Math.floor(resto / 60);
    const segundos = resto % 60;

    const hh = String(horas).padStart(2, '0');
    const mm = String(minutos).padStart(2, '0');
    const ss = String(segundos).padStart(2, '0');

    return `${dias} ${hh}:${mm}:${ss}`;
}

function setTotalTexto(texto = '00:00:00') {
    const el = document.getElementById('MoHrsTotal');
    if (!el) return;
    el.textContent = texto;
}

function renderLoading() {
    const container = document.getElementById('listaTiempos');
    if (!container) return;

    container.innerHTML = `
        <div class="list-group-item text-center text-muted">
            Cargando relojes...
        </div>
    `;

    setTotalTexto('00:00:00');
}

function renderEmpty(message = 'No se encontraron relojes para la falla.') {
    const container = document.getElementById('listaTiempos');
    if (!container) return;

    container.innerHTML = `
        <div class="list-group-item text-center text-muted">
            ${message}
        </div>
    `;

    setTotalTexto('00:00:00');
}

function renderClocks(rows = []) {
    const container = document.getElementById('listaTiempos');
    if (!container) return;

    if (!Array.isArray(rows) || rows.length === 0) {
        renderEmpty();
        return;
    }

    clocksState.rows = rows;

    let html = '';

    rows.forEach((item, index) => {
        html += `
            <label class="list-group-item d-flex align-items-center gap-3">
                <input
                    class="form-check-input me-2 reloj-check"
                    type="checkbox"
                    value="${item.TIEMPO || ''}"
                    data-index="${index}"
                >
                <div class="flex-grow-1">
                    <div class="fw-semibold">${item.NAME || '-'}</div>
                    <small class="text-muted">
                        ${item.TIEMPO || '00:00:00'} | ${item.HORAS ?? 0} hrs
                    </small>
                </div>
            </label>
        `;
    });

    container.innerHTML = html;
    setTotalTexto('00:00:00');
}

function getModalInstance() {
    const modalElement = document.getElementById('modalCalculo');
    if (!modalElement) return null;
    return bootstrap.Modal.getOrCreateInstance(modalElement);
}

export async function abrirModalRelojes(falla) {
    if (!falla) {
        console.warn('⚠️ No se recibió falla para consultar relojes');
        return;
    }

    const modal = getModalInstance();
    if (!modal) {
        console.warn('⚠️ No existe el modal #modalCalculo');
        return;
    }

    modal.show();
    renderLoading();

    try {
        const payload = await escalacionApi.obtenerClocksFalla(falla);

        if (!payload?.ok) {
            console.error('❌ Error clocks:', payload);
            renderEmpty(payload?.message || 'No se pudieron cargar los relojes.');
            return;
        }

        const rows = getData(payload);
        renderClocks(rows);
    } catch (error) {
        console.error('🔥 Error abrirModalRelojes:', error);
        renderEmpty('Error cargando relojes.');
    }
}

export function relojesCalcular() {
    const checks = document.querySelectorAll('.reloj-check:checked');

    if (!checks.length) {
        setTotalTexto('00:00:00');
        return;
    }

    let totalSegundos = 0;

    checks.forEach(check => {
        totalSegundos += parseTiempoToSeconds(check.value);
    });

    setTotalTexto(formatSecondsToTiempo(totalSegundos));
}

export function limpiarSeleccion() {
    document.querySelectorAll('.reloj-check').forEach(check => {
        check.checked = false;
    });

    setTotalTexto('00:00:00');
}

export function restarTiemposWO() {
    const totalTexto = document.getElementById('MoHrsTotal')?.textContent?.trim() || '00:00:00';
    const acumulado = document.getElementById('tiempoAcumulado')?.value?.trim() || '00:00:00';

    let resultadoSegundos = parseTiempoToSeconds(acumulado) - parseTiempoToSeconds(totalTexto);

    if (resultadoSegundos < 0) {
        resultadoSegundos = 0;
    }

    const resultado = formatSecondsToTiempo(resultadoSegundos);
    const inputTotalHoras = document.getElementById('totalHoras');

    if (inputTotalHoras) {
        const [, hhmmss = resultado] = resultado.split(' ');
        inputTotalHoras.value = hhmmss;
    }
}

export function registrarEventosClocks() {
    const btnCalcular = document.getElementById('btnCalcularRelojes');
    const btnLimpiar = document.getElementById('btnLimpiarRelojes');
    const btnRestar = document.getElementById('btnRestarRelojes');

    if (btnCalcular) {
        btnCalcular.addEventListener('click', relojesCalcular);
    }

    if (btnLimpiar) {
        btnLimpiar.addEventListener('click', limpiarSeleccion);
    }

    if (btnRestar) {
        btnRestar.addEventListener('click', restarTiemposWO);
    }
}
