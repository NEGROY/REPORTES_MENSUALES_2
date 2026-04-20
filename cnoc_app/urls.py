from django.urls import path, include
# ******************
# from cnoc_app.views import (
#     tablas_escalacion_view,
#     asientos_view,
#     retroalimentacion_view
# )
# ******************
from cnoc_app.views.login import login_view
from cnoc_app.views.home import home_view

 

# ----------------------------------------
urlpatterns = [
 # path('retroalimentacion/', include('cnoc_app.retroalimentacion.urls')),
 # path('escalacion/', include('cnoc_app.escalacion.urls')),
 # path('asientos/', include('cnoc_app.asientos.urls')),

 # #RUTRAS PARA EL HOME   
 # path('escalacion/tablas/', tablas_escalacion_view, name='tablas_escalacion'),
 # path('asientos/', asientos_view, name='asientos'),
 # path('retroalimentacion/', retroalimentacion_view, name='retroalimentacion'),

    # RUTAS DEL MENU PRINCIPAL 
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),


]
