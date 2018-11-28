from django.db import models

# Create your models here.
class Niveis(models.Model):
    nivel=models.CharField(max_length=50, null=False,blank=False , verbose_name='Nivel')
    def __str__(self):
        return self.nivel
    class Meta:
        verbose_name='Niveis'
    
class CompInfor(models.Model):
    tipoCompe=models.CharField(max_length=50,verbose_name='Competencia')
    software=models.CharField(max_length=50,verbose_name='Software')
    #Ollo comillas principiante
    nivel=models.ForeignKey(Niveis,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.software
    class Meta:
        verbose_name='Competencias informáticas'

class CompProg(models.Model):

    """
    Modelo que representas as competencias e nivel dos linguaxes de programación
    """
    linguaxe=models.CharField(max_length=50)
    nivel=models.ForeignKey(Niveis,on_delete=models.SET_NULL,blank=True,null=True)
    outra_info=models.TextField(blank=True, verbose_name='Informacion adicional')

    def __str__(self):
        return self.linguaxe
    class Meta:
        verbose_name='Linguaxes de programación'

class FormOficial (models.Model):
    titulacion=models.CharField(max_length=80)
    dataInicio=models.DateField(verbose_name='Data de inicio')
    dataFin=models.DateField(null=True,blank=True, verbose_name='Data finalización',help_text="En blanco se estás estudando na actualidade")
    escola=models.CharField(max_length=80, verbose_name='Centro de estudo')
    informacionAdicional=models.TextField()

    class Meta:
        ordering = ["dataFin","dataInicio"]
        verbose_name='Formación oficial'
    def __str__(self):
        return self.titulacion
    
class Curso(models.Model):
    nomeCurso=models.CharField(max_length=80, verbose_name='Nome do curso',blank=True, null=True )
    escola=models.CharField(max_length=80, verbose_name='Centro de estudo', blank=True, null=True)
    dataInicio=models.DateField(verbose_name='Data inicio' )
    dataFin=models.DateField(null=True,blank=True, verbose_name='Data finalización',help_text="En blanco se estás estudando na actualidade")
    duracion=models.CharField(max_length=6)
    compAdq=models.TextField(verbose_name='Competencias adquiridas')
    class Meta:
        ordering = ["dataFin","dataInicio"]
        verbose_name='Formación non oficial'
    def __str__(self):
        return self.nomeCurso

class Direccion(models.Model):
    rua=models.CharField(max_length=80, verbose_name='Rúa')
    numPis=models.IntegerField(verbose_name='Portal')
    andar=models.IntegerField(verbose_name='Piso')
    letraPis=models.CharField(max_length=1,verbose_name='Letra Piso')
    concello=models.CharField(max_length=40)
    provincia=models.CharField(max_length=40)

    def __str__(self):
        #return self.rua + ' %i ' +  self.concello + ' ' + self.provincia %self.numPis
        return '%s %i %i %s' % (self.rua, self.numPis,self.andar,self.concello)

class DatosPersoais(models.Model):

    nome=models.CharField(max_length=50)
    apel1=models.CharField(max_length=50 , verbose_name='1º Apelido')
    apel2=models.CharField(max_length=50, verbose_name='2º Apelido')
    dataNac=models.DateField(verbose_name='Data de nacemento')
    correoe=models.EmailField(verbose_name='Correo eléctronico')
    telefono=models.IntegerField(verbose_name='Numero de telefono',blank=True, null=True)

    def __str__(self):
        return self.nome + ' ' + self.apel1 + ' ' + self.apel2 
    class Meta:
        verbose_name='Datos persoais'

class Sector(models.Model):
    sector=models.CharField(max_length=50,blank=False,null=False)
    def __str__(self):
        return self.sector

class ExperienciaProfesional(models.Model):
    posto=models.CharField(max_length=80)
    empresa=models.CharField(max_length=80)
    provincia=models.CharField(max_length=50)
    concello=models.CharField(max_length=50)
    funcions=models.TextField()
    dataInicio=models.DateField(verbose_name='Data inicio')
    dataFin=models.DateField(null=True,blank=True, verbose_name='Data Finalización',help_text="En blanco se continúas na actualidade")
    sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, null=True)    
    def __str__(self):
        return self.posto + ' ' + self.empresa
    class Meta:
        ordering = ["dataFin","dataInicio"]
        verbose_name='Experiencia Profesional'

    #def get_absolute_url(self):
    
        #Devuelve el URL a una instancia particular de Book
        #El último método, get_absoulte_url() devuelve un URL que puede ser usado para acceder al detalle 
        #de un registro particular (para que esto funcione, debemos definir un mapeo de URL que tenga el 
        # nombre book-detail y una vista y una plantilla asociadas a él)
        
        #return reverse('posto', args=[str(self.id)])

class OutroDato(models.Model):
    texto1=models.CharField(max_length=50 , verbose_name='Dato de interés')
    texto2=models.TextField(verbose_name='Información adicional')
    def __str__(self):
        return self.texto1
    class Meta:
        verbose_name='Outros datos de interese'


class Curriculum(models.Model):
    datosPersoais=models.ForeignKey(DatosPersoais,on_delete=models.SET_NULL,null=True,blank=True)
    direccion=models.ForeignKey(Direccion,on_delete=models.SET_NULL,null=True,blank=True)
    experienciaProfesional=models.ManyToManyField(ExperienciaProfesional,null=True,blank=True)
    formOficial=models.ManyToManyField(FormOficial,null=True,blank=True)
    cursos=models.ManyToManyField(Curso,null=True,blank=True)
    compInfor=models.ManyToManyField(CompInfor,null=True,blank=True)
    compProg=models.ManyToManyField(CompProg,null=True,blank=True)
    OutroDato=models.ManyToManyField(OutroDato,null=True,blank=True)