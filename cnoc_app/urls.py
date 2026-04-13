from django.urls import path, include

urlpatterns = [
  #  path('retroalimentacion/', include('cnoc_app.retroalimentacion.urls')),
    path('escalacion/', include('cnoc_app.escalacion.urls')),
  #  path('asientos/', include('cnoc_app.asientos.urls')),
]
