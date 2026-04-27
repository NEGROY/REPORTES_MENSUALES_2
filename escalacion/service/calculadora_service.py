from escalacion.models import Escalacion

from .base_escalacion_service import BaseEscalacionService


class TablaCalculadoraService(BaseEscalacionService):
    def execute(self):
        area_id = self.kwargs.get('area_id')
        nivel_actual = self.parse_level(self.kwargs.get('nivel', 1))
        falla_data = self.kwargs.get('falla_data', {}) or {}

        if not area_id:
            return self.build_error_response('Debe seleccionar un área de escalación.')

        if not isinstance(falla_data, dict) or not falla_data:
            return self.build_error_response('No se recibieron datos de la falla.')

        hr_actual_raw = (
            falla_data.get('OPEN_TIME')
            or falla_data.get('open_time')
            or falla_data.get('F_UPDATE')
            or ''
        )
        hr_actual = self.parse_datetime(hr_actual_raw)

        if hr_actual is None:
            return self.build_error_response('No se pudo interpretar la fecha/hora base de la falla.')

        tmp_acumu = (
            falla_data.get('HH_MM_SS')
            or falla_data.get('TIEMPO_VIDA_TK')
            or falla_data.get('TIEMPO_SIN_SEGUIMIENTO_F')
            or ''
        )

        titulo = falla_data.get('TITULO') or falla_data.get('titulo') or ''
        falla_id = falla_data.get('TK') or falla_data.get('FALLA_ID') or falla_data.get('falla_id') or ''
        falla_dire = falla_data.get('TG_ENLACE_DESTINO') or falla_data.get('TG_ENLACE') or ''
        company = falla_data.get('COMPANY') or falla_data.get('company') or ''

        queryset = (
            Escalacion.objects
            .filter(area_id=area_id)
            .select_related('tipo_contacto', 'tipo_escalacion', 'area')
            .order_by('nivel')
        )

        if not queryset.exists():
            return self.build_error_response('No existen escalaciones configuradas para el área seleccionada.')

        rows = []
        permiso = self.kwargs.get('permiso', 0)

        for item in queryset:
            nivel_item = self.parse_level(item.nivel)
            tiempo_decimal = self.parse_decimal_hours(item.tiempo)

            if nivel_item >= nivel_actual:
                hr_suma = self.add_decimal_hours(hr_actual, tiempo_decimal)
            else:
                hr_suma = '00:00:00'

            comentario = item.comentario or ''
            tipo_medio = getattr(item.tipo_escalacion, 'tipo', '') if item.tipo_escalacion else ''
            nombre_area = getattr(item.area, 'nombre_area', '')

            action_data = {
                'hrActual': hr_actual.strftime('%Y-%m-%d %H:%M:%S'),
                'tmpAcumu': tmp_acumu,
                'areaSlct': str(area_id),
                'nivel': nivel_item,
                'nombre': getattr(item.tipo_contacto, 'nombre', ''),
                'telefono': getattr(item.tipo_contacto, 'telefono', ''),
                'tiempo': str(item.tiempo),
                'titulo': titulo,
                'comentario': comentario,
                'fallaID': falla_id,
                'hr_suma': hr_suma,
                'nombre_area': nombre_area,
                'permiso': permiso,
                'falla_dire': falla_dire,
                'company': company,
            }

            rows.append({
                'nivel': nivel_item,
                'nombre': getattr(item.tipo_contacto, 'nombre', ''),
                'telefono': getattr(item.tipo_contacto, 'telefono', ''),
                'tiempo': str(item.tiempo),
                'comentario': comentario,
                'tipo': tipo_medio,
                'nombre_area': nombre_area,
                'hr_suma': hr_suma,
                'action_data': action_data,
            })

        return self.build_success_response(
            {
                'rows': rows,
                'meta': {
                    'falla_id': falla_id,
                    'titulo': titulo,
                    'tmp_acumu': tmp_acumu,
                    'hr_actual': hr_actual.strftime('%Y-%m-%d %H:%M:%S'),
                    'area_id': str(area_id),
                    'nivel_actual': nivel_actual,
                    'falla_dire': falla_dire,
                    'company': company,
                }
            },
            'Tabla de escalación generada correctamente.'
        )
