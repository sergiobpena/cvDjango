from django.conf.urls import url
from django.urls import include, path
from . import views
from django.utils.translation import gettext_lazy as _



urlpatterns = [url(r'^$', views.index, name='index')]

urlpatterns +=[url(r'^perfil/$', views.PerfilView.as_view(), name='perfil')]

urlpatterns +=[url(r'^perfil/crea-experiencia/$', views.CrearExperienciaView.as_view(), name='crea-experiencia')]
urlpatterns +=[url(r'^perfil/crea-formoficial/$', views.CrearFormacionOficialView.as_view(), name='crea-formOficial')]
urlpatterns +=[url(r'^perfil/crea-curso/$', views.CrearCursoView.as_view(), name='crea-cursos')]
urlpatterns +=[url(r'^perfil/crea-datos/$', views.CreaDatosPersoaisView.as_view(), name='crea-datos')]
urlpatterns +=[url(r'^perfil/crea-direccion/$', views.CreaDireccionView.as_view(), name='crea-direccion')]
urlpatterns +=[url(r'^perfil/crea-comp-inform/$', views.CreaCompInfor.as_view(), name='crea-compInfo')]
urlpatterns +=[url(r'^perfil/crea-comp-prog/$', views.CreaCompProgView.as_view(), name='crea-comProg')]

urlpatterns+=[url(r'^perfil/edita-experiencia/(?P<pk>\d+)$', views.editaExperiencia, name='edita-experiencia')]
urlpatterns+=[url(r'^perfil/edita-formOficial/(?P<pk>\d+)$',views.EditaFormOficialView.as_view(),name='edita-formOficial')]
urlpatterns+=[url(r'^perfil/edita-curso/(?P<pk>\d+)$',views.EditaCursoView.as_view(),name='edita-curso')]
urlpatterns +=[url(r'^perfil/edita-datos/(?P<pk>\d+)$', views.EditaDatosPersoaisView.as_view(), name='edita-datos')]
urlpatterns +=[url(r'^perfil/edita-direccion/(?P<pk>\d+)$', views.EditaDireccionView.as_view(), name='edita-direccion')]
urlpatterns +=[url(r'^perfil/edita-comp-inform/(?P<pk>\d+)$', views.EditaCompInformView.as_view(), name='edita-compInfo')]
urlpatterns +=[url(r'^perfil/edita-comp-prog/(?P<pk>\d+)$', views.EditaCompProgView.as_view(), name='edita-comProg')]

urlpatterns+=[url(r'^perfil/borra-experiencia/(?P<pk>\d+)$', views.BorraExperienciaView.as_view(), name='borra-experiencia')]
urlpatterns+=[url(r'^perfil/borra-formOficial/(?P<pk>\d+)$',views.BorraFormOficialView.as_view(),name='borra-formOficial')]
urlpatterns+=[url(r'^perfil/borra-curso/(?P<pk>\d+)$',views.BorraCursoView.as_view(),name='borra-curso')]
urlpatterns +=[url(r'^perfil/borra-datos/(?P<pk>\d+)$', views.BorraDatosPersoaisView.as_view(), name='borra-datos')]
urlpatterns +=[url(r'^perfil/borra-direccion/(?P<pk>\d+)$', views.BorraDireccionView.as_view(), name='borra-direccion')]
urlpatterns +=[url(r'^perfil/borra-comp-inform/(?P<pk>\d+)$', views.BorraCompInformView.as_view(), name='borra-compInfo')]
urlpatterns +=[url(r'^perfil/borra-comp-prog/(?P<pk>\d+)$', views.BorraCompProgView.as_view(), name='borra-comProg')]
# urlpatterns+=[url(r'(?P<username>[\w.@+-]+)/form-oficial/(?P<pk>\d+)',views.EditaFormacionOficialView.as_view(),name='detalle-formOfi')]
# urlpatterns+=[url(r'(?P<pk>\d+)',views.EditaFormacionOficialView.as_view(),name='detalle-formOfi')]