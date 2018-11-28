from django.db import models

# Create your models here.
class Niveis(models.Model):
    nivel=models.CharField(max_length=50, null=False,blank=False)
    def __str__(self):
        return self.nivel
    
class CompInfor(models.Model):
    tipoCompe=models.CharField(max_length=50)
    software=models.CharField(max_length=50)
    #Ollo comillas principiante
    nivel=models.ForeignKey(Niveis,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.software

class Comp_Prog(models.Model):

    """
    Modelo que representas as competencias e nivel dos linguaxes de programación
    """
    linguaxe=models.CharField(max_length=50)
    nivel=models.ForeignKey(Niveis,on_delete=models.SET_NULL,blank=True,null=True)
    outra_info=models.TextField()

    def __str__(self):
        return self.linguaxe

class FormOficial (models.Model):
    titulacion=models.CharField(max_length=80)
    dataInicio=models.DateField()
    dataFin=models.DateField(null=True,blank=True)
    escola=models.CharField(max_length=80)
    informacionAdicional=models.TextField()

    class Meta:
        ordering = ["dataFin"]
    def __str__(self):
        return self.titulacion
    

class Curso(models.Model):
    nomeCurso:models.CharField(max_length=80)
    dataInicio=models.DateField()
    dataFin=models.DateField(null=True,blank=True)
    duracion=models.CharField(max_length=6)
    compAdq=models.TextField()
    class Meta:
        ordering = ["dataFin"]
    def __str__(self):
        return self.nomeCurso

class Direccion(models.Model):
    rua=models.CharField(max_length=80)
    numPis=models.IntegerField()
    andar=models.IntegerField()
    letraPis=models.CharField(max_length=1)
    concello=models.CharField(max_length=40)
    provincia=models.CharField(max_length=40)

    def __str__(self):
        return self.rua + ' ' + self.numPis + ' ' + self.andar + ' ' +  self.concello + ' ' + self.provincia

class DatosPersoais(models.Model):

    nome=models.CharField(max_length=50)
    apel1=models.CharField(max_length=50)
    apel2=models.CharField(max_length=50)
    dataNac=models.DateField()
    correoe=models.EmailField()

    def __str__(self):
        return self.nome + ' ' + self.apel1 + ' ' + self.apel2 

class Sector(models.Model):
    sector=models.CharField(max_length=50,blank=False,null=False)
    def __str__(self):
        return self.sector

class ExperienciaProfesional(models.Model):
    posto=models.TextField()
    empresa=models.TextField()
    provincia=models.CharField(max_length=50)
    concello=models.CharField(max_length=50)
    funcions=models.TextField()
    dataInicio=models.DateField()
    dataFin=models.DateField(null=True,blank=True)
    sector=models.CharField(max_length=50)
    sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, null=True)    
    def __str__(slelf):
        return self.posto + ' ' + self.empresa
    class Meta:
        ordering = ["dataFin"]

    #def get_absolute_url(self):
    
        #Devuelve el URL a una instancia particular de Book
        #El último método, get_absoulte_url() devuelve un URL que puede ser usado para acceder al detalle 
        #de un registro particular (para que esto funcione, debemos definir un mapeo de URL que tenga el 
        # nombre book-detail y una vista y una plantilla asociadas a él)
        
        #return reverse('posto', args=[str(self.id)])

class OutroDato(models.Model):
    texto1=models.CharField(max_length=50)
    texto2=models.TextField()
    def __str__(self):
        return self.texto1


class Curriculum(models.Model):
    datosPersoais=models.ForeignKey(DatosPersoais,on_delete=models.SET_NULL,null=True,blank=True)
    direccion=models.ForeignKey(Direccion,on_delete=models.SET_NULL,null=True,blank=True)
    experienciaProfesional=models.ManyToManyField(ExperienciaProfesional,null=True,blank=True)
    formOficial=models.ManyToManyField(FormOficial,null=True,blank=True)
    cursos=models.ManyToManyField(Curso,null=True,blank=True)
    compInfor=models.ManyToManyField(CompInfor,null=True,blank=True)
    compProg=models.ManyToManyField(Comp_Prog,null=True,blank=True)
    OutroDato=models.ManyToManyField(OutroDato,null=True,blank=True)