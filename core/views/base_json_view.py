import json

from django.http import JsonResponse
from django.views import View


class BaseJsonView(View):
    service_class = None
    success_status_code = 200
    error_status_code = 400

    def get_service_class(self):
        if self.service_class is None:
            raise NotImplementedError('Debe definir service_class en la vista hija.')
        return self.service_class

    def get_request_data(self, request):
        if request.method == 'GET':
            return request.GET.dict()

        if not request.body:
            return {}

        try:
            return json.loads(request.body.decode('utf-8'))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return {}

    def _normalize_recursive(self, value):
        if isinstance(value, dict):
            return {
                key: self._normalize_recursive(item)
                for key, item in value.items()
            }

        if isinstance(value, list):
            return [self._normalize_recursive(item) for item in value]

        if isinstance(value, str):
            return value.strip()

        return value

    def get_service_kwargs(self, request, *args, **kwargs):
        data = self.get_request_data(request)
        merged = {**kwargs, **data}
        return self._normalize_recursive(merged)

    def build_service(self, request, *args, **kwargs):
        service_class = self.get_service_class()
        return service_class(**self.get_service_kwargs(request, *args, **kwargs))

    def build_response(self, result):
        status_code = self.success_status_code if result.get('ok') else self.error_status_code
        return JsonResponse(result, status=status_code)

    def execute_service(self, request, *args, **kwargs):
        service = self.build_service(request, *args, **kwargs)
        result = service.execute()
        return self.build_response(result)

    def get(self, request, *args, **kwargs):
        return self.execute_service(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.execute_service(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.execute_service(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.execute_service(request, *args, **kwargs)