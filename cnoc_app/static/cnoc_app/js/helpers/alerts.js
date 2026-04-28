function hasSwal() {
    return typeof window.Swal !== 'undefined';
}

/* ALERTA SIMPLE */
export function showAlert({
    icon = 'info',
    title = '',
    text = '',
    timer = null,
    confirmButtonText = 'Aceptar',
    showConfirmButton = true,
}) {
    if (!hasSwal()) {
        console.warn('⚠️ SweetAlert2 no está cargado');
        alert(text || title || 'Alerta');
        return;
    }

    return Swal.fire({
        icon,
        title,
        text,
        timer,
        confirmButtonText,
        showConfirmButton,
    });
}

/* ALERTAS RÁPIDAS */
export function showSuccess(text = 'Proceso realizado correctamente.') {
    return showAlert({
        icon: 'success',
        text,
        timer: 1800,
        showConfirmButton: false,
    });
}

export function showError(text = 'Ocurrió un error.') {
    return showAlert({
        icon: 'error',
        text,
        timer: 2500,
        showConfirmButton: false,
    });
}

export function showWarning(text = 'Advertencia.') {
    return showAlert({
        icon: 'warning',
        text,
        timer: 2200,
        showConfirmButton: false,
    });
}

export function showInfo(text = 'Información.') {
    return showAlert({
        icon: 'info',
        text,
        timer: 2200,
        showConfirmButton: false,
    });
}

/* CONFIRMACIÓN */
export async function confirmAction({
    title = '¿Estás seguro?',
    text = '',
    icon = 'warning',
    confirmButtonText = 'Sí',
    cancelButtonText = 'Cancelar',
    confirmButtonColor = '#111111',
    cancelButtonColor = '#6c757d',
}) {
    if (!hasSwal()) {
        return confirm(text || title);
    }

    const result = await Swal.fire({
        title,
        text,
        icon,
        showCancelButton: true,
        confirmButtonText,
        cancelButtonText,
        confirmButtonColor,
        cancelButtonColor,
    });

    return result.isConfirmed;
}

/* LOADING */
export function showLoading(title = 'Procesando...') {
    if (!hasSwal()) {
        console.warn('⚠️ SweetAlert2 no está cargado');
        return;
    }

    Swal.fire({
        title,
        allowOutsideClick: false,
        allowEscapeKey: false,
        didOpen: () => {
            Swal.showLoading();
        },
    });
}

export function closeAlert() {
    if (!hasSwal()) return;
    Swal.close();
}

/* TOAST */
export function showToast({
    icon = 'success',
    title = '',
    timer = 2000,
    position = 'top-end',
}) {
    if (!hasSwal()) {
        console.warn('⚠️ SweetAlert2 no está cargado');
        return;
    }

    return Swal.fire({
        toast: true,
        position,
        icon,
        title,
        showConfirmButton: false,
        timer,
        timerProgressBar: true,
    });
}