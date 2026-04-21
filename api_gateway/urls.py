from django.urls import path

from .views import CnocCronologiaApiView

app_name = 'api_gateway'

urlpatterns = [
    path(
        'cnoc/cronologia/',
        CnocCronologiaApiView.as_view(),
        name='cnoc_cronologia'
    ),
]