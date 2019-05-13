from django.test import TestCase
from ..models import *
from django.contrib.auth.models import User

class PerfilVistasTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Definindo usuarios para as probas
        testUser1=User.objects.create_user(username='testuser1', password='12345abc',email='org@org.org')
        testUser1.save()
        testUser2=User.objects.create_user(username='testuser2', password='12345abc',email='org@org.org')
        testUser2.save()
        #define a base de datos de proba
        Sector.objects.create(
            sector='TIC'
        )
        Sector.objects.create(
            sector='Construccion'
        )
        Sector.objects.create(
            sector='Naval'
        )
        FormOficial.objects.create(
            titulacion='EGB Chucho',
            dataInicio='2006-06-01',
            dataFin='2008-06-01',
            escola='IES N 1',
            informacionAdicional='bla bla bla',
            usuario=testUser1
        )
        FormOficial.objects.create(
            titulacion='EGB Matias',
            dataInicio='2007-02-03',
            dataFin='2009-09-11',
            escola='IES N 2',
            informacionAdicional='ca ca ca',
            usuario=testUser2
        )
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
        ExperienciaProfesional.objects.create(
            posto='Ministro',
            empresa='Ghaviotas',
            provincia='Lugo',
            concello='Calvos de randin',
            funcions='Arreghlar o mundo',
            dataInicio='2006-06-01',
            dataFin='2008-06-01',
            sector=Sector.objects.get(pk=2),
            usuario=testUser1
        )
        Curso.objects.create(
            nomeCurso='Spring',
            escola='Unitaria Santacrus',
            dataInicio='2006-01-01',
            dataFin='2006-02-02',
            duracion='300 hrs',
            compAdq='Competentisimo',
            usuario=testUser1
        )
        Curso.objects.create(
            nomeCurso='Seguridad y salud',
            escola='Euroinnova',
            dataInicio='1997-04-04',
            dataFin='1999-05-05',
            duracion='50 hrs',
            compAdq='Tarjeta Construccion',
            usuario=testUser2
        )
        CompProg.objects.create(
            linguaxe="Java",
            nivel="p",
            outra_info='blabla',
            usuario=testUser1
        )

        CompProg.objects.create(
            linguaxe="R",
            nivel="p",
            outra_info='blabla',
            usuario=testUser1
        )

        CompInfor.objects.create(
            software='cad',
            tipoCompe='Cad',
            nivel="i",
            usuario=testUser2
        )
        DatosPersoais.objects.create(
            nome='Chucho',
            apel1='Raña',
            apel2='Rañolas',
            dataNac='1969-06-01',
            correoe='shuchoraña@gmail.com',
            telefono=666000666,
            usuario=testUser1
        )
        DatosPersoais.objects.create(
            nome='Matias',
            apel1='Rias',
            apel2='Rias',
            dataNac='1939-07-16',
            correoe='matiasrias@gmail.com',
            telefono=699000999,
            usuario=testUser2
        )
        Direccion.objects.create(
            rua='Porta Dos Condes,Queis',
            numPis=25,
            andar=0,
            letraPis='X',
            concello='Ordes',
            provincia='A Coruña',
            usuario=testUser1
        )
        Direccion.objects.create(
            rua='As Rias,Sobreira',
            numPis=15,
            andar=0,
            letraPis='X',
            concello='Ordes',
            provincia='A Coruña',
            usuario=testUser2
        )
    def loginTestUser1(self):
        self.client.login(username='testuser1', password='12345abc')

    def loginTestUser2(self):
        self.client.login(username='testuser2', password='12345abc')