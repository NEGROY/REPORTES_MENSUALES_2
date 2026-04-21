from core.services.cnoc import CronologiaService
from core.views.base_json_view import BaseJsonView


class CnocCronologiaApiView(BaseJsonView):
    service_class = CronologiaService

    def get_service_kwargs(self, request, *args, **kwargs):
        data = super().get_service_kwargs(request, *args, **kwargs)

        return {
            'ticket': data.get('ticket') or data.get('falla_id', ''),
        }
