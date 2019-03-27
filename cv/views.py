from django.shortcuts import render

# Create your views here.

from .models import CompInfor , CompProg , FormOficial , Curso , Direccion , DatosPersoais , Sector , ExperienciaProfesional , OutroDato , Curriculum

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_compInfor=CompInfor.objects.all().count()
    num_compProg=CompProg.objects.all().count()
    num_cursos=Curso.objects.all().count()
    num_experiencia=ExperienciaProfesional.objects.all().count()
    num_datout=OutroDato.objects.all().count()
    num_formOficial=FormOficial.objects.all().count()

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
        'num_compInfor':num_compInfor,
        'num_compProg':num_compProg,
        'num_experiencia':num_experiencia,
        'num_datout':num_datout,
        'num_formOficial':num_formOficial,
        'num_visits':num_visits
        },
    )
    
from django.views import generic

class ExperienciaProfesionalView(generic.ListView):
    model = ExperienciaProfesional
    context_object_name='exp_profes' #nome da lista para a variable de plantilla
    #queryset=ExperienciaProfesional.objects.filter(concello__icontains='santiago')[:1]
    template_name = 'cv/experiencia.html'
    #def get_queryset(self, **kwargs):
        #context = super(ExperienciaProfesionalView, self).get_context_data(**kwargs)
        #context['some_data'] = 'This is just some data'
        #return context
class ExperienciaProfesionalViewDetalles(generic.ListView):
    model=ExperienciaProfesional
    template_name = 'cv/experiencia_detalle.html'
    

from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#@login_required
class ExperienciaProfesionalCrearView(LoginRequiredMixin,CreateView):
    model=ExperienciaProfesional
    fields='__all__'
    template_name = 'cv/experiencia_form.html'
    success_url='./'
""" class XestionCvCrearView(LoginRequiredMixin,CreateView):
    model=Curriculum
    fields='__all__'
    template_name = ''
    success_url='./' """

""" from .forms import CreateUserForm
class Create(CreateView):
    success_url = reverse_lazy('login')
    template_name = '/sign_up.html'
    model = User
    form_class = CreateUserForm

def form_valid(self,form):
    self.object = form.save(commit=False)
    self.object.set_password(self.object.password)
    self.object.save()
    return HttpResponseRedirect(self.get_success_url()) """
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ContactoForm

def mensaxeContacto(request):
    if request.method=='POST':
        formulario=ContactoForm(request.POST)

"""


    