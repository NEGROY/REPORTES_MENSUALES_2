from abc import ABC
from datetime import datetime, timedelta
from decimal import Decimal, InvalidOperation

from core.services.base.base_service import BaseService


class BaseEscalacionService(BaseService, ABC):
    def build_success_response(self, data, message='Consulta realizada correctamente.'):
        return {
            'ok': True,
            'message': message,
            'data': data,
        }

    def build_error_response(self, message, error=None):
        payload = {
            'ok': False,
            'message': message,
        }
        if error:
            payload['error'] = error
        return payload

    def parse_datetime(self, value: str | None):
        if not value:
            return None

        formatos = [
            '%Y-%m-%dT%H:%M:%S',
            '%Y-%m-%d %H:%M:%S',
            '%Y-%m-%dT%H:%M',
            '%Y-%m-%d %H:%M',
        ]

        for fmt in formatos:
            try:
                return datetime.strptime(str(value).strip(), fmt)
            except ValueError:
                continue

        return None

    def parse_decimal_hours(self, value):
        try:
            return Decimal(str(value).strip())
        except (InvalidOperation, AttributeError):
            return Decimal('0')

    def add_decimal_hours(self, base_dt, hours_decimal: Decimal):
        if base_dt is None:
            return ''

        hours = int(hours_decimal)
        minutes_decimal = (hours_decimal - Decimal(hours)) * Decimal('60')
        minutes = int(minutes_decimal.quantize(Decimal('1')))

        return (base_dt + timedelta(hours=hours, minutes=minutes)).strftime('%Y-%m-%d %H:%M:%S')

    def parse_level(self, value):
        try:
            return int(str(value).strip())
        except (ValueError, TypeError):
            return 1