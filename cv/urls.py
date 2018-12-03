from django.conf.urls import url

from . import views



#(^ es un marcador de inicio de cadena y  $ es un marcador de fin de cadena). 
#La función  url() también especifica un parámetro name, que identifica de manera única  este mapeador de URL particular.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^experiencia/$', views.ExperienciaProfesionalView.as_view(), name='experiencia'),
    url(r'^experiencia/(?P<pk>\d+)$', views.ExperienciaProfesionalViewDetalles.as_view(), name='detalle-experiencia'),
    url(r'^crea-experiencia/$', views.ExperienciaProfesionalCrearView.as_view(), name='crea-experiencia'),
]