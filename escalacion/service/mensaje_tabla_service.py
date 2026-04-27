from .base_escalacion_service import BaseEscalacionService
from ..models import Escalacion


class MensajeTablaService(BaseEscalacionService):
    def execute(self):
        area_id = self.kwargs.get('area_id')
        hr_actual_raw = self.kwargs.get('hr_actual')
        titulo = self.kwargs.get('titulo', '')
        falla_id = self.kwargs.get('falla_id', '')
        permiso = self.kwargs.get('permiso', 0)

        if not area_id:
            return self.build_error_response('Debe enviar el área de escalación.')

        if not hr_actual_raw:
            return self.build_error_response('Debe enviar la hora actual.')

        hr_actual = self.parse_datetime(hr_actual_raw)
        if hr_actual is None:
            return self.build_error_response('No se pudo interpretar la hora actual.')

        queryset = (
            Escalacion.objects
            .filter(area_id=area_id)
            .select_related('tipo_contacto', 'tipo_escalacion', 'area')
            .order_by('nivel')
        )

        if not queryset.exists():
            return self.build_error_response('No existen escalaciones configuradas para el área seleccionada.')

        nombre_area = getattr(queryset.first().area, 'nombre_area', '')

        tabla_txt = []
        tabla_txt.append('=' * 95)
        tabla_txt.append(f' ÁREA: {nombre_area}')
        tabla_txt.append(f' TABLA DE ESCALACIÓN |: {titulo} (Falla ID: {falla_id})')
        tabla_txt.append('=' * 95)
        tabla_txt.append(
            f"| {'No.':<3} | {'Nombre':<25} | {'Teléfono':<13} | {'Tiempo':<10} | "
            f"{'Hr Suma':<19} | {'Tipo':<15} | {'Comentario':<25} |"
        )
        tabla_txt.append('-' * 95)

        for item in queryset:
            comentario = item.comentario or ''
            tiempo_decimal = self.parse_decimal_hours(item.tiempo)
            hr_suma = self.add_decimal_hours(hr_actual, tiempo_decimal)

            nombre = getattr(item.tipo_contacto, 'nombre', '')[:25]
            telefono = getattr(item.tipo_contacto, 'telefono', '')[:13]
            tipo = getattr(item.tipo_escalacion, 'tipo', '')[:15] if item.tipo_escalacion else ''
            nivel = str(item.nivel)
            tiempo = f"{item.tiempo} hrs"
            comentario_txt = comentario[:25]

            fila = (
                f"| {nivel:<3} | "
                f"{nombre:<25} | "
                f"{telefono:<13} | "
                f"{tiempo:<10} | "
                f"{hr_suma:<19} | "
                f"{tipo:<15} | "
                f"{comentario_txt:<25} |"
            )
            tabla_txt.append(fila)

        tabla_txt.append('=' * 95)

        return self.build_success_response(
            {
                'texto': '\n'.join(tabla_txt)
            },
            'Mensaje de tabla generado correctamente.'
        )