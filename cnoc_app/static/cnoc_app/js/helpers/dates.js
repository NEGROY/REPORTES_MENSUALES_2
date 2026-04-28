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