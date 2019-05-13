from django.test import TestCase
from ..models import *
from ..views.view_perfil import *
from django.contrib.auth.models import User
from django.urls import resolve
from .inicializacion_test import PerfilVistasTestCase

'''
Test da paxina de perfil

'''

class PerfilTestClass(PerfilVistasTestCase):

    def setUp(self):
        super().loginTestUser1()

    def test_perfilStatusCode(self):

        uerrele=reverse('perfil')
        response=self.client.get(uerrele)
        self.assertEquals(response.status_code,200)

    def test_urlResolverPerfil(self):
        '''
        Comproba que o mapeo de perfil funciona
        '''
        view = resolve('/cv/perfil')
        self.assertEquals(view.func, PerfilView.as_view())


class ExperienciaProfesionalTestClass (PerfilVistasTestCase):

    def setUp(self):
        super().loginTestUser1()

    def test_experieciaProfesionalstatusCode(self):

        url=reverse('crea-experiencia')
        response=self.client.get(url)
        self.assertEquals(response.status_code,200)
    def test_urlResolverCreaExperiencia(self):

        view=resolve('/cv/perfil/crea-experiencia')

        self.assertEquals(view.func,CrearExperienciaView.as_view())
    def test_crsf(self):
        '''
        Comproba que esta protexido con crsf
        '''
        url = reverse('crea-experiencia')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

