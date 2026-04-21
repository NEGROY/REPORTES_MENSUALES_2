from abc import ABC

from core.db.oracle.dboracle import sql_execution
from core.services.base import BaseService


class BaseCnocService(BaseService, ABC):
    query_class = None

    def get_query_class(self):
        if self.query_class is None:
            raise NotImplementedError('Debe definir query_class en la clase hija.')
        return self.query_class

    def build_query(self):
        query_class = self.get_query_class()
        return query_class(**self.kwargs)

    def run_select(self):
        query = self.build_query()
        return sql_execution(
            query.get_sql(),
            tipo=0,
            parametros=query.get_params()
        )

    def build_success_response(self, data, message='Consulta realizada correctamente.'):
        return {
            'ok': True,
            'message': message,
            'data': data,
        }

    def build_error_response(self, message, error=None):
        response = {
            'ok': False,
            'message': message,
        }

        if error:
            response['error'] = error

        return response