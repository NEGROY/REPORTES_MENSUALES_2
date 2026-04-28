/**
 * Formatea fechas tipo:
 * 2025-08-11T07:43:41
 *
 * Modos soportados:
 * - display            -> 11/08/2025 07:43:41
 * - sql                -> 2025-08-11 07:43:41
 * - datetime-local     -> 2025-08-11T07:43
 * - date               -> 2025-08-11
 * - time               -> 07:43:41
 */
export function formatDateValue(value, mode = 'display') {
    if (!value) return '';

    const str = String(value).trim();
    // Soporta:
    // 2025-08-11T07:43:41
    // 2025-08-11 07:43:41
    const match = str.match(
        /^(\d{4})-(\d{2})-(\d{2})[T\s](\d{2}):(\d{2})(?::(\d{2}))?$/
    );

    if (!match) { return str; }
    const [, yyyy, mm, dd, hh, min, ss = '00'] = match;

    switch (mode) {
        case 'sql':
            return `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss}`;

        case 'datetime-local':
            return `${yyyy}-${mm}-${dd}T${hh}:${min}`;

        case 'date':
            return `${yyyy}-${mm}-${dd}`;

        case 'time':
            return `${hh}:${min}:${ss}`;

        case 'display':
        default:
            return `${dd}/${mm}/${yyyy} ${hh}:${min}:${ss}`;
    }
}


/**
 * Normaliza fecha para enviarla al backend Django
 * Devuelve:
 * - YYYY-MM-DD HH:MM:SS
 * - HH:MM:SS
 * - cadena vacía si no es válida
 */
export function normalizeDateForBackend(value) {
    if (!value) return '';

    const str = String(value).trim();

    // datetime-local o sql datetime
    const fullMatch = str.match(
        /^(\d{4})-(\d{2})-(\d{2})[T\s](\d{2}):(\d{2})(?::(\d{2}))?$/
    );

    if (fullMatch) {
        const [, yyyy, mm, dd, hh, min, ss = '00'] = fullMatch;
        return `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss}`;
    }

    // solo hora
    const timeMatch = str.match(/^(\d{2}):(\d{2})(?::(\d{2}))?$/);
    if (timeMatch) {
        const [, hh, min, ss = '00'] = timeMatch;
        return `${hh}:${min}:${ss}`;
    }

    return '';
}


/* HORAS DE TIEMPO ACTUAL  */
export function getCurrentDateTimeLocal() {
    const now = new Date();
    const yyyy = now.getFullYear();
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const dd = String(now.getDate()).padStart(2, '0');
    const hh = String(now.getHours()).padStart(2, '0');
    const min = String(now.getMinutes()).padStart(2, '0');

    return `${yyyy}-${mm}-${dd}T${hh}:${min}`;
}
