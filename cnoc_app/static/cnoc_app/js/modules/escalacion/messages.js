import { escalacionApi } from './api.js';


function setValue(id, value) {
    const el = document.getElementById(id);
    if (!el) return;

    el.value = (value === null || value === undefined) ? '' : String(value);
}

function safeValue(id) {
    const el = document.getElementById(id);
    if (!el) return '';
    return (el.value || '').trim();
}

export function mnsjEscala(data = {}) {
    console.log('🟢 mnsjEscala ejecutada', data);

    const tiempo = safeValue('tiempoAcumulado');
    const tiempoWO = safeValue('totalHoras');

    const mensaje = `*## ESCALACION ${data.nivel ?? ''} ##*
${data.nivel ?? ''}\t${data.nombre ?? ''}\t${data.telefono ?? ''}\t${data.tiempo ?? ''}Hrs\t${data.hr_suma ?? ''} Hrs

*${data.titulo ?? ''}*
SE INDICA TIEMPO Y CLIENTES`;

    const wasapp = `*DETALLES DE LA ESCALACIÓN DE FALLA*
Se escala con ${data.nombre ?? ''}
${data.nivel ?? ''} ${data.nombre ?? ''} ${data.telefono ?? ''} ${data.tiempo ?? ''}hrs ${data.hr_suma ?? ''}Hrs

*FALLA Masiva* : ${data.fallaID ?? ''}
*FALLA General* : F-

*TIEMPO DE LA FALLA MASIVA*: ${tiempo}
${data.titulo ?? ''}

*CLIENTES AFECTADOS*: -

*SEGUIMIENTO*:`;

    const mensajeWo = `**ESCALACIÓN**
**TICKET:** ${data.fallaID ?? ''}
**CLIENTE:** ${data.company ?? ''}
**DIRECCIÓN:** ${data.falla_dire ?? ''}
**ÁREA RESPONSABLE:** ${data.nombre_area ?? ''}

ESCALACIÓN:
${data.nivel ?? ''} ${data.nombre ?? ''} ${data.telefono ?? ''} ${data.tiempo ?? ''}hrs ${data.hr_suma ?? ''}Hrs

**ESTADO ACTUAL:** [Agregar estado actual]
**TIEMPO ACUMULADO:** ${data.tmpAcumu ?? ''} Hrs @${data.telefono ?? ''}
**TIEMPO TOTAL WO:** ${tiempoWO} Hrs @${data.telefono ?? ''}`;

    const mensajeGeneral = `**TICKET:** ${data.fallaID ?? ''}
**CLIENTE:** ${data.company ?? ''}
**DIRECCIÓN:** ${data.falla_dire ?? ''}
**ÁREA RESPONSABLE:** ${data.nombre_area ?? ''}

**ESCALACIÓN:** ${data.nombre ?? ''} ${data.telefono ?? ''} ${data.hr_suma ?? ''}
**ESCALACIÓN NIVEL:** ${data.nivel ?? ''}

**TIEMPO TOTAL:** ${data.tmpAcumu ?? ''}
**TIEMPO TOTAL WO:** ${tiempoWO}

**DIAGNÓSTICO ACTUAL:**`;

    setValue('notaGenerada', mensaje);
    setValue('wasapp', wasapp);
    setValue('notaGenerada3', Number(data.permiso) === 5 ? mensajeWo : mensajeGeneral);

        tb_copy(
            data.titulo,
            data.fallaID,
            data.hrActual,
            data.tmpAcumu,
            data.areaSlct
        );
    
    console.log('✅ Mensajes generados correctamente');
}

/* --> FUNCION PARA QUE COPEYEN LAS TBALAS   */
export async function tb_copy(titulo, fallaID, hrActual, tmpAcumu, areaSlct) {
    try {
        const payload = await escalacionApi.generarMensajeTabla({
            titulo: titulo,
            falla_id: fallaID,
            hr_actual: hrActual,
            tmp_acumu: tmpAcumu,
            area_id: areaSlct,
        });

        if (!payload?.ok) {
            console.error('❌ Error generando mensaje de tabla:', payload);
            return;
        }

        const texto = payload?.data?.texto || '';
        setValue('notaGenerada2', texto);

        console.log('✅ tabla texto generada', {
            titulo,
            fallaID,
            hrActual,
            tmpAcumu,
            areaSlct,
        });
    } catch (error) {
        console.error('🔥 Error tb_copy:', error);
    }
}
