from django.test import TestCase
from ..models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class FormOficialTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("Test Formación oficial")

    def setUp(self):
        testUser1=User.objects.create_user(username='testuser1', password='12345abc',email='org@org.org')
        testUser1.save()

        # usuario=authenticate(username='testuser1',password='12345abc')
        FormOficial.objects.create(
            titulacion='EGB',
            dataInicio='2006-06-01',
            dataFin='2008-06-01',
            escola='IES N 1',
            informacionAdicional='bla bla bla',
            usuario=testUser1
        )
    def test_compUrl(self):
        formacion=FormOficial.objects.get(id=1)
        self.assertEquals(formacion.get_absolute_url(),'/cv/perfil/edita-formOficial/1')

class ExperienciaTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Test Experiencia Profesional")


    def setUp(self):
        testUser1 = User.objects.create_user(username='testuser1', password='12345abc', email='org@org.org')
        testUser1.save()
        Sector.objects.create(sector='Construccion')
        ExperienciaProfesional.objects.create(
            posto='Alicatador',
            empresa='Chapuzas e ghaliñeiros',
            provincia='A Coruña',
            concello='A Peroxa',
            funcions='Chapucear',
            dataInicio='2006-06-01',
            dataFin='2008-06-01',
            sector=Sector.objects.get(pk=1),
            usuario=testUser1
        )
    def test_obterurl(self):
        experiencia=ExperienciaProfesional.objects.get(pk=1)
        self.assertEquals(experiencia.get_absolute_url(),'/cv/perfil/edita-experiencia/1')



class CursoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("Test Experiencia Profesional")

    def setUp(self):
        testUser1 = User.objects.create_user(username='testuser1', password='12345abc', email='org@org.org')
        testUser1.save()
        Curso.objects.create(
            nomeCurso='Spring',
            escola='Euroinnova',
            dataInicio='2006-01-01',
            dataFin='2006-02-02',
            duracion='300 hrs',
            compAdq='Competentisimo',
            usuario=testUser1
        )
# class compInformTest(TestCase):
#     def setUp(self):
#         testUser1=User.objects.create_user(username='testuser1', password='12345abc',email='org@org.org')
#         testUser1.save()
#         CompInfor.objects.create(
#             tipoCompe='Cad',
#             software='Autocad',
#             nivel='p',
#             usuario=testUser1
#         )